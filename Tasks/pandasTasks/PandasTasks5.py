import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import (
    OneHotEncoder,
    OrdinalEncoder,
    MinMaxScaler,
    StandardScaler,
    RobustScaler
)

from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline

np.random.seed(42)

customer_data = pd.DataFrame({
    'customer_id': range(1, 1001),
    'registration_date': pd.date_range('2022-01-01', periods=1000, freq='D'),
    'age': np.random.randint(18, 70, 1000),
    'income': np.random.normal(50000, 20000, 1000),
    'last_login': pd.date_range('2023-01-01', periods=1000, freq='H'),
    'total_orders': np.random.poisson(10, 1000),
    'total_spent': np.random.exponential(500, 1000),
    'avg_order_value': None,
    'preferred_category': np.random.choice(['Electronics', 'Clothing', 'Books'], 1000)
})

purchase_history = pd.DataFrame({
    'customer_id': np.random.choice(range(1, 1001), 5000),
    'purchase_date': pd.date_range('2023-01-01', periods=5000, freq='H'),
    'amount': np.random.exponential(100, 5000),
    'category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home'], 5000)
})

print("--- Initial customer_data head ---")
print(customer_data.head())
print("\n--- Initial purchase_history head ---")
print(purchase_history.head())

# Part 1: Feature Engineering Workshop

# Task 1: Calculate avg_order_value and fill missing values
customer_data['avg_order_value'] = customer_data['total_spent'] / customer_data['total_orders']
customer_data.replace([np.inf, -np.inf], 0, inplace=True)
customer_data['avg_order_value'].fillna(0, inplace=True)

print("\n--- Task 1: customer_data with calculated 'avg_order_value' ---")
print(customer_data[['customer_id', 'total_spent', 'total_orders', 'avg_order_value']].head())

# Task 2: Create recency features
snapshot_date = purchase_history['purchase_date'].max() + pd.Timedelta(days=1)
customer_data['days_since_last_login'] = (snapshot_date - customer_data['last_login']).dt.days

last_purchase_dates = purchase_history.groupby('customer_id')['purchase_date'].max().reset_index()
last_purchase_dates.rename(columns={'purchase_date': 'last_purchase_date'}, inplace=True)
customer_data = pd.merge(customer_data, last_purchase_dates, on='customer_id', how='left')
customer_data['days_since_last_purchase'] = (snapshot_date - customer_data['last_purchase_date']).dt.days
customer_data['days_since_last_purchase'].fillna(999, inplace=True)

print(f"\n--- Task 2: Recency features calculated against snapshot date: {snapshot_date.date()} ---")
print(customer_data[['customer_id', 'last_login', 'days_since_last_login', 'last_purchase_date', 'days_since_last_purchase']].head())

# Task 3: Create frequency features
purchase_counts = purchase_history.groupby('customer_id').size().reset_index(name='purchase_frequency')
customer_data = pd.merge(customer_data, purchase_counts, on='customer_id', how='left')
customer_data['purchase_frequency'].fillna(0, inplace=True)
customer_data['account_age_days'] = (snapshot_date - customer_data['registration_date']).dt.days

print("\n--- Task 3: customer_data with frequency features ---")
print(customer_data[['customer_id', 'purchase_frequency', 'registration_date', 'account_age_days']].head())

# Task 4: Create monetary features
customer_data['spending_velocity'] = customer_data['total_spent'] / customer_data['account_age_days']
customer_data['spending_velocity'].fillna(0, inplace=True)

preferred_category = purchase_history.groupby('customer_id')['category'].agg(lambda x: x.mode()[0]).reset_index()
preferred_category.rename(columns={'category': 'actual_preferred_category'}, inplace=True)
customer_data = pd.merge(customer_data, preferred_category, on='customer_id', how='left')

print("\n--- Task 4: customer_data with monetary features ---")
print(customer_data[['customer_id', 'total_spent', 'account_age_days', 'spending_velocity', 'actual_preferred_category']].head())

# Task 5: Create age groups and income brackets
age_labels = ['18-30', '31-45', '46-60', '61+']
customer_data['age_group'] = pd.cut(customer_data['age'], bins=[17, 30, 45, 60, 70], labels=age_labels)
income_labels = ['Low', 'Medium', 'High', 'Very High']
customer_data['income_bracket'] = pd.qcut(customer_data['income'], q=4, labels=income_labels)

print("\n--- Task 5: customer_data with binned features ---")
print(customer_data[['age', 'age_group', 'income', 'income_bracket']].head())

# Task 6: Build RFM (Recency, Frequency, Monetary) analysis features
rfm_df = pd.DataFrame({
    'customer_id': customer_data['customer_id'],
    'Recency': customer_data['days_since_last_purchase'],
    'Frequency': customer_data['purchase_frequency'],
    'Monetary': customer_data['total_spent']
})

rfm_df['R_score'] = pd.qcut(rfm_df['Recency'], 4, labels=[4, 3, 2, 1])
rfm_df['F_score'] = pd.qcut(rfm_df['Frequency'].rank(method='first'), 4, labels=[1, 2, 3, 4])
rfm_df['M_score'] = pd.qcut(rfm_df['Monetary'], 4, labels=[1, 2, 3, 4])
rfm_df['RFM_Segment'] = rfm_df['R_score'].astype(str) + rfm_df['F_score'].astype(str) + rfm_df['M_score'].astype(str)

print("\n--- Task 6: RFM Segmentation DataFrame ---")
print(rfm_df.head())

# Task 7: Create seasonal shopping patterns
purchase_history['purchase_month'] = purchase_history['purchase_date'].dt.month_name()
seasonal_preference = purchase_history.groupby('customer_id')['purchase_month'].agg(lambda x: x.mode()[0]).reset_index()
seasonal_preference.rename(columns={'purchase_month': 'peak_shopping_month'}, inplace=True)
customer_data = pd.merge(customer_data, seasonal_preference, on='customer_id', how='left')

print("\n--- Task 7: customer_data with seasonal preference ---")
print(customer_data[['customer_id', 'peak_shopping_month']].head())

# Task 8: Engineer interaction features
customer_data['age_income_interaction'] = customer_data['age'] * customer_data['income']

print("\n--- Task 8: customer_data with interaction feature ---")
print(customer_data[['age', 'income', 'age_income_interaction']].head())


# Part 2: Categorical Encoding Challenge
data = pd.DataFrame({
    'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], 1000),
    'education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], 1000),
    'job_title': np.random.choice(['Manager', 'Developer', 'Analyst', 'Designer', 'Sales'], 1000),
    'company_size': np.random.choice(['Small', 'Medium', 'Large'], 1000),
    'experience_level': np.random.choice(['Entry', 'Mid', 'Senior', 'Executive'], 1000),
    'salary': np.random.normal(70000, 30000, 1000)
})

print("\n\n--- Part 2: Categorical Encoding Challenge ---")
print("Initial Categorical DataFrame:")
print(data.head())

# Task 2: Apply appropriate encoding
education_map = {'High School': 0, 'Bachelor': 1, 'Master': 2, 'PhD': 3}
company_size_map = {'Small': 0, 'Medium': 1, 'Large': 2}
experience_level_map = {'Entry': 0, 'Mid': 1, 'Senior': 2, 'Executive': 3}
data['education_ordinal'] = data['education'].map(education_map)
data['company_size_ordinal'] = data['company_size'].map(company_size_map)
data['experience_level_ordinal'] = data['experience_level'].map(experience_level_map)

print("\n--- After Ordinal Encoding ---")
print(data[['education', 'education_ordinal', 'experience_level', 'experience_level_ordinal']].head())

data_one_hot = pd.get_dummies(data, columns=['city', 'job_title'], prefix=['city', 'job'])

print("\n--- After One-Hot Encoding (showing new columns) ---")
print(data_one_hot.filter(regex='city_|job_').head())

job_salary_map = data.groupby('job_title')['salary'].mean().to_dict()
data['job_title_target_encoded'] = data['job_title'].map(job_salary_map)

print("\n--- After Target Encoding (Demonstration) ---")
print(data[['job_title', 'job_title_target_encoded', 'salary']].head())

# Task 4 & 5: Handle unseen categories and create a preprocessing pipeline
X = data[['city', 'education', 'job_title', 'company_size', 'experience_level']]
y = data['salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

ordinal_cols = ['education', 'company_size', 'experience_level']
nominal_cols = ['city', 'job_title']

ordinal_order = [
    ['High School', 'Bachelor', 'Master', 'PhD'],
    ['Small', 'Medium', 'Large'],
    ['Entry', 'Mid', 'Senior', 'Executive']
]

preprocessor = ColumnTransformer(transformers=[
    ('ord', OrdinalEncoder(categories=ordinal_order), ordinal_cols),
    ('nom', OneHotEncoder(handle_unknown='ignore'), nominal_cols)
])

pipeline = Pipeline(steps=[('preprocessor', preprocessor)])
pipeline.fit(X_train)
X_train_transformed = pipeline.transform(X_train)
X_test_transformed = pipeline.transform(X_test)

print("\n--- Task 5: Pipeline Transformation Result ---")
print("Shape of transformed training data:", X_train_transformed.shape)
print("Shape of transformed test data:", X_test_transformed.shape)
print("\nFirst 5 rows of transformed data (sparse matrix):")
print(X_train_transformed[:5])

# Part 3: Scaling and Normalization Challenge
numerical_features = customer_data[['age', 'income', 'total_spent', 'total_orders', 'purchase_frequency']]

print("\n\n--- Part 3: Scaling and Normalization Challenge ---")
print("Initial Numerical DataFrame for Scaling:")
print(numerical_features.describe())

# Task 1: Analyze the distribution of each feature
print("\n--- Task 1: Feature Distribution Plots ---")
numerical_features.hist(bins=30, figsize=(15, 10))
plt.suptitle("Histograms of Numerical Features")
plt.show()

# Task 2, 3, 4: Apply different scaling methods
scaled_features = pd.DataFrame()
df = numerical_features.copy()

min_max_scaler = MinMaxScaler()
scaled_features['age_minmax'] = min_max_scaler.fit_transform(df[['age']])

std_scaler = StandardScaler()
scaled_features['income_standard'] = std_scaler.fit_transform(df[['income']])

robust_scaler = RobustScaler()
scaled_features['total_spent_robust'] = robust_scaler.fit_transform(df[['total_spent']])

print("\n--- Tasks 2, 3, 4: Description of Scaled Features ---")
print(scaled_features.describe())

# Task 5: Compare the effect of different scaling methods
df_compare = pd.DataFrame()
df_compare['Original'] = df['total_spent']
df_compare['MinMax'] = MinMaxScaler().fit_transform(df[['total_spent']])
df_compare['Standard'] = StandardScaler().fit_transform(df[['total_spent']])
df_compare['Robust'] = RobustScaler().fit_transform(df[['total_spent']])

plt.figure(figsize=(12, 6))
sns.kdeplot(data=df_compare)
plt.title("Comparison of Scaling Methods on 'total_spent'")
plt.show()

print("\n--- Task 5: Visual Comparison ---")
print("The plot above shows that scaling changes the range and center of the data, but not the shape of its distribution.")


# Task 6: Handle outliers before scaling
df_clean = df.copy()

Q1 = df_clean['total_spent'].quantile(0.25)
Q3 = df_clean['total_spent'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers_removed = df_clean[(df_clean['total_spent'] >= lower_bound) & (df_clean['total_spent'] <= upper_bound)]

print(f"\n--- Task 6: Outlier Handling ---")
print(f"Original number of rows: {len(df_clean)}")
print(f"Number of rows after removing outliers: {len(outliers_removed)}")
print(f"Number of outliers removed: {len(df_clean) - len(outliers_removed)}")

scaler = StandardScaler()
outliers_removed['total_spent_scaled'] = scaler.fit_transform(outliers_removed[['total_spent']])
print("\nDescription of 'total_spent' after outlier removal and scaling:")
print(outliers_removed[['total_spent', 'total_spent_scaled']].describe())

# Task 7 & 8: Create a complete preprocessing pipeline and test on new data
X = numerical_features
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

scaling_preprocessor = ColumnTransformer(transformers=[
    ('minmax', MinMaxScaler(), ['age']),
    ('standard', StandardScaler(), ['income']),
    ('robust', RobustScaler(), ['total_spent', 'total_orders', 'purchase_frequency'])
], remainder='passthrough')

scaling_pipeline = Pipeline(steps=[('scaler', scaling_preprocessor)])
scaling_pipeline.fit(X_train)
X_train_scaled = scaling_pipeline.transform(X_train)
X_test_scaled = scaling_pipeline.transform(X_test)

scaled_columns = ['age', 'income', 'total_spent', 'total_orders', 'purchase_frequency']
X_test_scaled_df = pd.DataFrame(X_test_scaled, columns=scaled_columns, index=X_test.index)

print("\n--- Task 7 & 8: Pipeline Results ---")
print("Original test data head:")
print(X_test.head())
print("\nScaled test data head (transformed using parameters learned from training data):")
print(X_test_scaled_df.head())
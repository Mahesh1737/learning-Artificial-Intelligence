import pandas as pd
import numpy as np

# 10. Data Transformation Tasks

# Sample DataFrames
df_customers = pd.DataFrame({
    'name': ['joHN DOE', 'JANE_smith', 'ALICE-jOHNSON'],
    'address': ['123 Main St, New York, NY 10001', '456 Oak Ave, Boston, MA 02118', '789 Pine Rd, Austin, TX 73301'],
    'phone': ['1234567890', '(987)654-3210', '555-123-4567'],
    'email': ['John.Doe@Gmail.com', 'jane_smith@outlook.COM', 'alice-j@Yahoo.com']
})

df_transactions = pd.DataFrame({
    'customer_id': [1, 2, 3, 1],
    'amount': [1500, 75, 500, 120],
    'currency': ['USD', 'EUR', 'USD', 'GBP'],
    'timestamp': pd.to_datetime(['2025-09-20 10:00', '2025-09-21 15:30',
                                  '2025-09-22 08:15', '2025-09-22 21:00'])
})

# print("Original Customers DataFrame:", df_customers)
# print("\nOriginal Transactions DataFrame:", df_transactions)

#Complex String Processing
#Standardize names
# df_customers['name'] = df_customers['name'].str.replace(r'[_-]', ' ', regex=True).str.title()
# print(df_customers['name'])

# # 2. Parse addresses
# df_customers[['street', 'city', 'state_zip']] = df_customers['address'].str.split(',', expand=True)
# df_customers[['state', 'zip']] = df_customers['state_zip'].str.strip().str.split(' ', n=1, expand=True)
# print(df_customers[['street', 'city', 'state', 'zip']])


# # 3. Standardize phone numbers
# df_customers['phone'] = df_customers['phone'].str.replace(r'\D', '', regex=True).str.replace(
#     r'(\d{3})(\d{3})(\d{4})', r'(\1) \2-\3', regex=True)
# print(df_customers['phone'])


# # 4. Clean and standardize emails
# df_customers['email'] = df_customers['email'].str.strip().str.lower()
# print(df_customers['email'])

# # 5. Extract domain
# df_customers['domain'] = df_customers['email'].str.split('@').str[1]
# print(df_customers['domain'])   


# # 10.2 Advanced Function Application
# # 1. Categorize transactions
# def categorize(amount):
#     if amount > 1000:
#         return 'large'
#     elif amount >= 100:
#         return 'medium'
#     else:
#         return 'small'
# df_transactions['category'] = df_transactions['amount'].apply(categorize)
# print(df_transactions['category'])

# # 2. Convert to USD (mock rates)
# rates = {'USD': 1, 'EUR': 1.1, 'GBP': 1.3}
# df_transactions['amount_usd'] = df_transactions.apply(lambda x: x['amount'] * rates[x['currency']], axis=1)
# print(df_transactions['amount_usd'])


# # 3. Time-based features
# df_transactions['hour'] = df_transactions['timestamp'].dt.hour
# df_transactions['day_of_week'] = df_transactions['timestamp'].dt.day_name()
# df_transactions['is_weekend'] = df_transactions['timestamp'].dt.dayofweek >= 5
# df_transactions['is_business_hours'] = df_transactions['hour'].between(9, 17)
# print(df_transactions[['hour', 'day_of_week', 'is_weekend', 'is_business_hours']])


# # 11. Combining Datasets Tasks

# # Sample orders
df_orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104],
    'customer_id': [1, 2, 3, 2],
    'product': ['Laptop', 'Phone', 'Tablet', 'Headphones'],
    'amount': [1200, 800, 300, 100]
})

# # 1. Customer report
# customer_report = df_customers.copy()
# customer_report['total_orders'] = df_orders.groupby('customer_id')['order_id'].transform('count')
# customer_report['total_spent'] = df_orders.groupby('customer_id')['amount'].transform('sum')
# print(customer_report)


# # 3. Product performance
# product_performance = df_orders.groupby('product')['amount'].agg(['sum', 'mean', 'count'])
# print(product_performance)


# # 5. Order details with customer info
# order_details = df_orders.merge(df_customers, left_on='customer_id', right_index=True, how='left')
# print(order_details)

# 13. Grouping and Aggregation Tasks

# # Sales data
df_sales = pd.DataFrame({
    'region': ['North', 'South', 'North', 'East', 'West', 'South'],
    'salesperson': ['Alice', 'Bob', 'Alice', 'Charlie', 'David', 'Bob'],
    'quarter': [1, 1, 2, 2, 3, 3],
    'category': ['Electronics', 'Clothing', 'Electronics', 'Furniture', 'Electronics', 'Clothing'],
    'sales': [5000, 2000, 7000, 3000, 4000, 1000]
})

# # 1. Monthly sales (simulate by grouping by region)
# monthly_sales = df_sales.groupby('region')['sales'].sum()
# print(monthly_sales)


# # 3. Category analysis
# category_trends = df_sales.groupby('category')['sales'].agg(['sum', 'mean'])
# print(category_trends)


# # 4. Commission
# df_sales['commission'] = df_sales['sales'] * 0.05
# print(df_sales[['sales', 'commission']])


# # 5. Underperforming
# underperforming = df_sales.groupby('region')['sales'].sum().sort_values().head(1)
# print(underperforming)


# # ---- School Data Example ----
df_scores = pd.DataFrame({
    'school': ['A', 'A', 'B', 'B', 'B', 'C'],
    'student': ['s1', 's2', 's3', 's4', 's5', 's6'],
    'grade': [90, 70, 80, 60, 85, 95]
})

# # 11. Normalize scores within school
# df_scores['normalized'] = df_scores.groupby('school')['grade'].transform(lambda x: (x - x.mean()) / x.std())
# print(df_scores[['school', 'student', 'grade', 'normalized']])

# # 12. Rank within grade level
# df_scores['rank'] = df_scores.groupby('school')['grade'].rank(ascending=False)
# print(df_scores[['school', 'student', 'grade', 'rank']])

# # 13. Avg school performance
# df_scores['school_avg'] = df_scores.groupby('school')['grade'].transform('mean')
# print(df_scores[['school', 'student', 'grade', 'school_avg']])

# # 14. Best/worst performing students
best_worst = df_scores.loc[df_scores.groupby('school')['grade'].idxmax()]
worst = df_scores.loc[df_scores.groupby('school')['grade'].idxmin()]
print("Best performing students:\n", best_worst[['school', 'student', 'grade']])
print("Worst performing students:\n", worst[['school', 'student', 'grade']])
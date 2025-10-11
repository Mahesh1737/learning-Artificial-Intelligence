import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

df = pd.read_csv("Machine Learning/UnsupervisedLearning/Mall_Customers.csv")
print("Dataframe : \n",df.head())

#preprocess data


# 1. Check for missing values
print("Missing values:\n", df.isnull().sum())

# 2. Drop CustomerID (not useful for clustering)
df = df.drop('CustomerID', axis=1)

# 3. Encode categorical variables (Gender)
df = pd.get_dummies(df, columns=['Gender'], drop_first=True)
print("After encoding:\n", df.head())

# 4. Feature scaling (Age, Annual Income, Spending Score)
scaler = StandardScaler()
X_Scaled = scaler.fit_transform(df)
df_scaled = pd.DataFrame(X_Scaled, columns=df.columns)
print("Scaled features:\n", df_scaled.head())

# 5. Save the preprocessed data
df_scaled.to_csv("Machine Learning/UnsupervisedLearning/Mall_Customers_preprocessed.csv", index=False)
print("Preprocessed data saved.")


#pairplot

sns.pairplot(df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']])
plt.show()


# Determine WCSS (within clusters sum of squares) for each value of K
wcss = []
for k in range(2, 11):
    kmeans = KMeans (n_clusters=k, random_state=42)
    kmeans.fit(X_Scaled)
    wcss.append(kmeans.inertia_)

# Plot the Elbow curve
plt.plot(range(2, 11), wcss, marker='o', linestyle='--')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')
plt.title('Elbow Method')
plt.show()


for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X_Scaled)
    score = silhouette_score(X_Scaled, labels)
    print(f"For K = {k}, silhouette_score = {score}")
    
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_Scaled)


#view the cluster
print(df.head())

#Cluster center
print("Cluster center : ",kmeans.cluster_centers_)
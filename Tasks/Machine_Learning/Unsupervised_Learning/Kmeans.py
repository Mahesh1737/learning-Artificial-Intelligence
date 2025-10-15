import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Load the dataset
df = pd.read_csv("Tasks/Machine_Learning/Supervise_Learning/datasets/Ice_cream selling data.csv")
print("Dataframe : \n", df.head())

# 1. Check for missing values
print("Missing values:\n", df.isnull().sum())

# 2. Feature scaling
scaler = StandardScaler()
X_Scaled = scaler.fit_transform(df)
df_scaled = pd.DataFrame(X_Scaled, columns=df.columns)
print("Scaled features:\n", df_scaled.head())

# 3. Save the preprocessed data
df_scaled.to_csv("Tasks/Machine_Learning/Supervise_Learning/datasets/Ice_cream_selling_preprocessed.csv", index=False)
print("Preprocessed data saved.")

# 4. Scatter plot of the data
plt.scatter(df['Temperature (°C)'], df['Ice Cream Sales (units)'], c='blue', alpha=0.6)
plt.xlabel('Temperature (°C)')
plt.ylabel('Ice Cream Sales (units)')
plt.title('Ice Cream Sales vs Temperature')
plt.show()

# 5. Determine WCSS (within clusters sum of squares) for each value of K
wcss = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_Scaled)
    wcss.append(kmeans.inertia_)

# Plot the Elbow curve
plt.plot(range(2, 11), wcss, marker='o', linestyle='--')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')
plt.title('Elbow Method')
plt.show()

# 6. Silhouette scores for each K
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X_Scaled)
    score = silhouette_score(X_Scaled, labels)
    print(f"For K = {k}, silhouette_score = {score}")

# 7. Fit final KMeans (choose K=4 as example)
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_Scaled)

# View the cluster assignment
print(df.head())

# Cluster centers (in scaled space)
print("Cluster centers (scaled):", kmeans.cluster_centers_)
import pandas as pd
import matplotlib.pylab as plt
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA

# step1
df = pd.read_csv("Machine Learning/UnsupervisedLearning/Mall_Customers.csv")
print(df)

# step 2
df = df.drop("CustomerID", axis=1)
df["Gender"] = LabelEncoder().fit_transform(df["Gender"])


# step 3
X = df.values

# step 4
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#step 5
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Step 6
pca_df = pd.DataFrame(data=X_pca, columns=["PC1", "PC2"])
print(pca_df)

# step 7
plt.figure(figsize=(8,6))
plt.scatter(pca_df["PC1"], pca_df["PC2"], c='blue', edgecolors='k', alpha=0.7)
plt.xlabel("Principle components 1")
plt.ylabel("Principle components 2")
plt.title("PCA mall customer 2d projecction")
plt.grid(True)
plt.show()


# step 8

print("Explained vairance by components : ", pca.explained_variance_ratio_)
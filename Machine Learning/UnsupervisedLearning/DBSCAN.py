import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pylab as plt
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score#used to evaluate clustering quality
#(between -1 and 1, hight is better)

X, y_true = make_blobs(n_samples=300, cluster_std=0.60, centers=4, random_state=42)
#X =: Features cordinates of points

#y_true =: True cluster labels(we dont use in unsupervised learning)

scaler = StandardScaler()

X_Scaled = scaler.fit_transform(X)
#Now every feature has a mean 0 and std 1

#Creates DBSCAN model:

#eps =0.3 -> radius of neighbourhood
#min_samples = 5 -> minimum points need to form cluster
dbscan = DBSCAN(eps=0.3, min_samples=5)

labels = dbscan.fit_predict(X_Scaled)

plt.figure(figsize=(8,6))

plt.scatter(X_Scaled[:,0], X_Scaled[:, 1], c=labels, cmap='plasma', s=50)
plt.title('Dbscan clusting resut')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.grid(True)
plt.show()



#Clustring evaluation

mask = labels != -1
#creates a mask to filter out noise points (-1 labels)
if len(set(labels)) > 1 and np.any(mask):
    #Checks if there aer at least two clusters and some noe-noise points
    score = silhouette_score(X_Scaled[mask], labels[mask])
    print(f"Silhouetter score : {score:.3f}")
else:
    print("Silhouette score is not applicable (only noise or one cluster detectedd)")
    
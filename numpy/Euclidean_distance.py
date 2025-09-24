import numpy as np
# Example points (2D coordinates)
points = np.array([[0, 0],
[1, 1],
[2,2],
[3, 3]])

# Compute distance matrix
dist_matrix = np.sqrt((((points[:, np.newaxis,:] - points [np.hewaxis, :, : ])) **2).sum(axis=2))

print("Distance Matrix: \n", dist_matrix)
import numpy as np

data = np.array([5, 10, 15, 20, 25, 30])

normalized = (data-np.min(data))/((np.max(data))-(np.min(data)))

print("Normalized data: ", normalized)
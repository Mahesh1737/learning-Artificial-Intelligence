import numpy as np
# Create an array with random integers
arr = np.random.randint(10, 100, size=10) 
print("Original Array:", arr)
# Replace values > 50 with o
arr[arr > 50] = 0
print("Modified Array:", arr)
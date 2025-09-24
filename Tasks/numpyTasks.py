import numpy as np


# Create a 1D array of numbers from 10 to 50
arr_10_to_50 = np.arange(10, 51)
print("1D array from 10 to 50:\n", arr_10_to_50)

# # Create a 3x3 identity matrix
identity_matrix = np.identity(3)
print("\n3x3 identity matrix:\n", identity_matrix)

# # Create an array of 10 zeros and 10 ones
zeros = np.zeros(10)
ones = np.ones(10)
zeros_and_ones = np.concatenate([zeros, ones])
print("\nArray of 10 zeros and 10 ones:\n", zeros_and_ones)




# # Reshape a 1D array of 25 elements into a 5x5 matrix
arr_25_elements = np.arange(25)
matrix_5x5 = arr_25_elements.reshape(5, 5)
print("\nReshaped 5x5 matrix:\n", matrix_5x5)

# Horizontally and vertically stack two arrays
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])

# h_stack = np.hstack((a, b))
# print("\nHorizontally stacked arrays:\n", h_stack)

# v_stack = np.vstack((a, b))
# print("\nVertically stacked arrays:\n", v_stack)

# # Flatten a 2D array into a 1D array
# flattened_array = matrix_5x5.flatten()
# print("\nFlattened 2D array:\n", flattened_array)



# # Set the seed value so random numbers are reproducible
# # Any number can be used as a seed. Using the same seed will always
# # produce the same sequence of random numbers.
# np.random.seed(42)

# # Generate an array of 20 random integers between 1 and 100
# random_integers = np.random.randint(1, 101, 20)
# print("\n20 random integers between 1 and 100 (with seed):\n", random_integers)

# # Create a 4x4 matrix with random values between 0 and 1
# random_matrix_4x4 = np.random.rand(4, 4)
# print("\n4x4 matrix with random values between 0 and 1:\n", random_matrix_4x4)
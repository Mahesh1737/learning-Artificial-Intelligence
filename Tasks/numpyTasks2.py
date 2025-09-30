import numpy as np

#Task1

# arr = np.array([23, 45, 67, 89, 12, 90, 11, 78])

# arr[50 < arr] = 0

# print(arr)


#Task2

# arr = np.array([11, 3, 10, 23, 45, 67, 89, 12, 90, 11, 78])
# def prime_num(n):
#     if n<2:
#         return False
#     for i in range(2, int(np.sqrt(n))+1):
#         if(n%i==0):
#             return False
#     return True

# prime_check = np.vectorize(prime_num)

# prime_numbers = arr[prime_check(arr)]

# print("Prime numbers: ", prime_numbers)

#Task3

# arr = np.array([[11, 3, 10], [23, 45, 67], [89, 12, 90], [11, 78, 44]])

# a = np.array([2, 3, 4])

# result = arr + a
# print(result)

#Task4


# arr = np.array([[11, 3, 10], [23, 45, 67], [89, 12, 90], [11, 78, 44]])

# a = np.array([2, 3, 4])

# result = arr * a
# print(result)


#Task5
# arr = np.array([5, 10, 15, 20, 25, 30])

# normalized = (arr-min(arr))/((max(arr))-(min(arr)))
# print("Normalized data: ", normalized)

#Task6 
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# window = 3

# mov_avg = np.convolve(arr, np.ones(window)/window, mode = 'valid')

# print("Moving average: ", mov_avg)

#Tassk7

points = np.array([[0, 0],
[1, 1],
[2,2],
[3, 3]])

dist_matrix = np.sqrt((((points[:, np.newaxis,:] - points [np.newaxis, :, : ])) **2).sum(axis=2))

print("Distance Matrix: \n", dist_matrix)
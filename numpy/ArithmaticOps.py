import numpy as np

#by using + operator
# firstArray = np.array([1,2,3,4,5,6])
# secondArray = np.array([7,8,9,5,6,7,])
# addition = firstArray + secondArray
# print("Addition of the firstArray and secondArray : ",addition)

# #by using add function
# firstArray = np.array([1,2,3,4,5,6])
# secondArray = np.array([7,8,9,5,6,7,])
# addition =np.add(firstArray,secondArray)
# print("Addition of the firstArray and secondArray : ",addition)

# #exponent operations
# a = np.array([1,2,3,4,5,6])
# b = a**2
# print("Usesing the ** operator : ",b)

# a = np.array([1,2,3,4,5,6])
# b = a.power(2)
# print("Usesing the power : ",b)


#Modulo
firstArray = np.array([1,2,3,4,5,6])
secondArray = np.array([7,8,9,5,6,7,])

a = firstArray % secondArray
print(a)

b = np.mod(firstArray, secondArray)
print(b)
import numpy as np
#create a seq of intfrom 0 to 30 with step 5
f = np.arange(0, 30, 5)
print("A sequential array with steps of 5:\n", f)

#linspace()
#create a seq of 10 values in range 0 to 5
g = np.linspace(0, 5, 10)
print ("A sequential array with 10 values between"
       "0 and 5:\n", g)

# #reshape NumPy Array 
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3) 
print(reshaped)

arr = np.array([1,2,3,4,5,6,7,8,9])
newarr = arr.reshape(3, 3)
print(newarr)


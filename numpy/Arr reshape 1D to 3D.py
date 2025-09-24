import numpy as np
#create1D
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
#print
print("Array : "+str(array))
#reshape numpy array
#converting it to 3D from 1D
reshaped = array.reshape((2,2,4))
#print
print("Reshaped 3-D Array :")
print(reshaped)

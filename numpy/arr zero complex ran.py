import numpy as np
c=np.zeros((3,4))
print("Array initialized with all zeros:", c)

d=np.full((3,3), 6, dtype = 'complex')
print ("An array initialized with all 6s."
       "Array type is complex:\n", d)

e=np.random.random((2,2))
print("A random array:\n", e)

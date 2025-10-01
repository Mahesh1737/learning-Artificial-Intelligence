import matplotlib.pyplot as plt
import numpy as np

# plt.plot([1, 2, 3, 4], [5, 6, 7, 8])
# plt.ylabel('some numbers')
# plt.xlabel('some numbers')
# plt.show()  

# Adding legends and titles

x = [1,3, 6]
y = [2, 10, 5]
x2 = [1,4,6]
y2 = [3, 7, 9]

plt.plot(x, y, label='line 1')
plt.plot(x2, y2, label='line 2')    
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Multiple Lines Example')
plt.legend()    
plt.show()
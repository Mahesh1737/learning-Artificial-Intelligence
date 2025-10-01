import matplotlib.pyplot as plt
import numpy as np  
# Bar Chart Example
x = ['A', 'B', 'C', 'D']
y1 = [3, 7, 5, 12]
y2 = [4, 6, 8, 10]
bar_width = 0.35
x_indices = np.arange(len(x))
plt.bar(x_indices, y1, width=bar_width, color='skyblue', label='Bar 1')
plt.bar(x_indices + bar_width, y2, width=bar_width, color='salmon', label='Bar 2')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Dual Bar Chart Example')
plt.legend()
plt.show()
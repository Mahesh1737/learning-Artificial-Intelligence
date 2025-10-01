import matplotlib.pyplot as plt
import numpy as np  

# Bar Chart Example
x = ['A', 'B', 'C', 'D']
y = [3, 7, 5, 12]
plt.bar(x, y, color='skyblue', label='Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.legend()
plt.show()


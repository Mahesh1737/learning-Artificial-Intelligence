import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
data = np.random.randn(1000)

# Scatter Plot
plt.figure(figsize=(12, 5)) 
plt.subplot(1, 2, 1)
plt.scatter(x, np.sin(x), color='blue', label='sin(x)', alpha=0.5)
plt.scatter(x, np.cos(x), color='red', label='cos(x)', alpha=0.5)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Scatter Plot Example')
plt.legend()
plt.grid(True)
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Sample data
age = [22, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 34, 56, 23, 45, 67, 89, 90, 100, 34, 23, 45, 56, 78, 88, 99]
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Histogram
plt.hist(age, bins, color='blue', histtype='bar', rwidth=0.8, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()
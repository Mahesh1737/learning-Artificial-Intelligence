import numpy as np

data = np.array([10,20,30,40, 50, 60])

window = 3

moving_avg = np.convolve(data, np.ones(window)/window, mode='valid')

print("Moving average : ",moving_avg)

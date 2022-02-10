# importing the required libraries
import matplotlib.pyplot as plt
import numpy as np

# define data values
x = np.array([1, 2, 3, 4])  # X-axis points
y = x * 2  # Y-axis points

plt.plot(x, y)  # Plot the chart
plt.show()  # display
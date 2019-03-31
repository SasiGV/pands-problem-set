#Sasikala Varatharajan - G00376470

#Program to print plot of functions x, x2 and 2x in the range[0, 4]

#Import numpy arrays to  store the range values
#Import Matplot library to use matplot functions 
import numpy as np
import matplotlib.pyplot as plt

#Arange range values
x = np.arange(0,4)

#Define different variables for the given functions
y = x
y1 = x**2
y2 = 2**x

#Arange the values in a plot
plt.plot(x, y, x, y1, x, y2, '.-')

#Label x-axis and y-axis and add title
plt.xlabel('Values of X')
plt.ylabel('Values of Y')
plt.title('Histogram of functions x, x^2 and 2^x')
#Set grid to True to view the grid on the plot
plt.grid(True)

#Show the plot
plt.show()
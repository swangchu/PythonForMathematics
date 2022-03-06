# Graph the function f(x) = 5x – 3.
# y = 5*x -3

import matplotlib.pyplot as plt

import numpy as np

x = np.linspace(-2,3,100)

y = 5 * x - 3

plt.plot(x, y, '-r', label='y = 5 * x - 3')

plt.title('Graph of y = 5 * x - 3')

plt.xlabel('x', color='#1C2833')

plt.ylabel('y', color='#1C2833')

plt.legend(loc='upper left')

plt.grid()

plt.show()

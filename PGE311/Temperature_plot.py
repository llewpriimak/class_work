import numpy as np
import matplotlib.pyplot as plt

def temp_plot():

    variables = np.array([[2.04, -1, 0, 0],[-1,2.04,-1,0],[0, -1, 2.04, -1],[0, 0, -1, 2.04]])
    b = np.array([40.8, 0.8, 0.8, 200.8])
    x = np.linalg.solve(variables,b)
    plt.xlabel('X points') ; plt.ylabel('Temperature')
    plt.grid(True)
    plt.plot(x)

    plt.show()

temp_plot()
import numpy as np
import matplotlib.pyplot as plt


def f(x,y):
    return 0.15*y
# Runge Kutta's method for solving initial value problems
#  dy/dx=f(x,y)
#  y(x0) = y0
#  on interval [x0,xn] with spacing h.
#  The method returns arrays x and y with corresponding
#  values of x and y(x).
def runge_kutta_method(x0, xn, y0, h, f):
    # discretize [x0,xn]
    x = np.arange(x0, xn + h, h)
    # reserve space for y's that we are looking for
    y = np.zeros(x.shape)
    y[0] = y0
    n = len(x)

    for i in range(0, n - 1):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + 0.5 * h, y[i] + k1 * 0.5 * h)
        k3 = f(x[i] + 0.5 * h, y[i] + k2 * 0.5 * h)
        k4 = f(x[i] + h, y[i] + k3 * h)

        slope = (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y[i + 1] = y[i] + slope * h

    return (x, y)

x,y = runge_kutta_method(150,240,150,1,f)
print(x,y)
plt.plot(y,x)
plt.show()
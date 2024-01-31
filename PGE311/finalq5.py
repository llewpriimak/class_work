import numpy as np
import matplotlib.pyplot as plt


def f1(x, y, z):
    return (1-y**2)*z + y

def f2(x, y, z):
    return z


def euler_method_system(x0, xn, y0, z0, h, f1, f2):
    x = np.arange(x0, xn + h, h)
    y = np.zeros(x.shape)
    z = np.zeros(x.shape)

    z[0] = y0
    z[0] = z0
    n = len(x)

    for i in range(0, n - 1):
        y[i + 1] = y[i] + f1(x[i], y[i], z[i]) * h
        z[i + 1] = z[i] + f2(x[i], z[i], y[i]) * h

    return (x, y, z)

x,y,z = euler_method_system(0,10,1,1,0.2,f1,f2)
x1,y1,z1 = euler_method_system(0,10,1,1,0.1,f1,f2)

plt.plot(x,y,'r-', label = 'x,y h = 0.2')
plt.plot(x,z,'b-',label = 'x,z h = 0.2')
plt.plot(x1,y1,'g-',label = 'x,y h = 0.1')
plt.plot(x1,z1,'y-',label = 'x,z h = 0.1')
plt.grid('True'); plt.xlabel = 'X';plt.ylabel = 'Y'
plt.legend()
plt.show()

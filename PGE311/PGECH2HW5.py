
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pylab




# This function with calculate the angle between two
# vectors
def oned_two_vector_angle():
    
    u = np.array([-2,1,3])
    v = np.array([3,1,2])
    u_norm = np.linalg.norm(u)
    v_norm = np.linalg.norm(v)
    cos_theta = np.dot(u, v) / (u_norm * v_norm)
    print(cos_theta)
    radians = np.arccos(cos_theta)
    print(np.degrees(radians))
    return np.degrees(radians)
    

    

#oned_two_vector_angle()

#z = np.linspace(-4, 4, 10000)

#y = (1/np.sqrt(2*np.pi)) * np.exp(-((z**2)/2))

#print(np.max(y))
#plt.grid(True)
#plt.xlabel('z')
#plt.ylabel('F(z)')
#plt.plot(z, y)

def manning_equation():
    
    x = np.array([[0.035,0.0001,10,2.0],[0.020,0.0002,8,1.0],[0.015,0.0010,20,1.5],[0.030,0.0007,24,3.0],[0.022,0.0003,15,2.5]])
    u = (np.sqrt(x[:,1])/x[:,0]) * np.power((x[:,2]) * x[:,3]/(x[:,2]+ 2 * x[:,3]), 2/3)
    print(u)
    print(x)
    print(x[:,2])
   

manning_equation()

def hw5q4():

    v = np.linspace(10,80,8)
    F = np.array([25,75,380,550,610,1220,830,1450])
    v_calc = np.linspace(0,100,50)
    F_calc = 0.274*v_calc**1.984
    plt.grid(True)
    plt.plot(v,F,c='w',marker='o',mfc='m',mec='m')
    plt.plot(v_calc,F_calc,c='k',lw=1.)
    plt.xlabel('velocity ‐ m/s')
    plt.ylabel('force ‐ N')
    plt.loglog(v, F, c='w', marker='o', mfc='m', mec='m')
    plt.loglog(v_calc, F_calc, c='k', lw=1.)

    
# hw5q4()

def hw5q5():

    t = np.arange(0,100,1/16)
    x = np.sin(t)*(np.exp(np.cos(t)) - (2*np.cos(4*t)) - np.power(np.sin(t/12), 5))
    y = np.cos(t)*(np.exp(np.cos(t)) - (2*np.cos(4*t)) - np.power(np.sin(t/12), 5))

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Butterfly Curve Plot 2')
    plt.grid(True)
    # plt.axis([-4, 4, -4, 4])
    plt.plot(t, x, '-', c = 'k', label = 'x')
    plt.plot(t, y,':', c ='k', label ='y')
    # plt.plot(x, y, label = 'butterfly')
    plt.legend()

hw5q5()
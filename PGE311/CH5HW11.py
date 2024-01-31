import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import roots

def q1(h, t = 2.5):

    g = 9.81
    L = 4
    t = 2.5
    return (np.power(2 * g * h, 0.5) * np.tanh(np.power((g*h)/L,0.5) * t)) - 5

def plot1():

    h_points = np.linspace(0,6,100)
    plt.plot(h_points, q1(h_points,1))
    plt.plot(h_points, q1(h_points, 2))
    plt.plot(h_points, q1(h_points, 3))
    plt.plot(h_points, q1(h_points, 4))
    plt.plot(h_points, q1(h_points, 5))
    plt.grid(True)
    plt.xlabel('h level') ; plt.ylabel('Velocity')
    plt.show()


#plot1()

def q2():

    return roots.bisection_method(q1,0,4, )

q2()

def q3_helper(x):

    return np.log(x**2) - 0.7

def q3():
    #roots.bisection_method(q3_helper,0.5, 2)
    roots.false_position_method(q3_helper,0.5, 2)

#q3(

def q6_helper(T):

    return 0.99403 + (1.671 * (1/np.power(10,4) * T)) + (9.7215 * ((1/np.power(10,8)) * np.power(T,2))) -(9.5838 * ((1/np.power(10,11)) * np.power(T,3)))+ (1.92520 * ((1/np.power(10,14)) * np.power(T,4))) - 1.1

def q6():
    x = np.arange(0,1200, 1)
    plt.plot(x, q6_helper(x))
    plt.grid(True)
    plt.show()


#q6()

def q7():
    roots.bisection_method(q6_helper,0, 1300)

#q7()
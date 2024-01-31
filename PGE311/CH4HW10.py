import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt

#Question 3 answer towards the bottom

x = 0.577
y = (6*x)/(np.power(1-3*(x**2), 2))

print(y)
print(((y-2350000)/y) * 100)
print(((y - 2352000)/y)*100)

# x = (np.pi/3)
# y = 1 - ((x**2)/2) + ((x**4)/math.factorial(4)) - (x**6)/math.factorial(6) + (x**8)/math.factorial(8)
# #print(y)
#
# E = -0.5
# approx = 1
#
# true_val = E + approx
# #print(true_val)
#
# e_t = ((true_val - approx)/true_val) * 100
# #print(e_t)
#
# print(((0.5021 - 0.4516886)/0.5021) * 100)

def bisection_method(f, xl, xu, eps=0.0125):

    # Initialize the function
    err = xu - xl
    it = 0
    max_it = 10000
    xm = (xl + xu) / 2

    # Execute the iterations
    while err > eps and it < max_it:
        xm = (xl + xu) / 2
        it += 1

        if f(xl) * f(xm) <= 0:
            xu = xm
        elif f(xm) * f(xu) <= 0:
            xl = xm
        else:
            print('f(xm) is likely 0')
            xu = xm
            xl = xm

        err = xu - xl
    #print('The root approximation is', xm, 'The number of iterations:', it)
    return xm, it, err


# plot the function to visualize the bounds for the bisection method
def plot_func():

    x = np.linspace(-10000,10000,1000)
    y = (x**2) - (5000.002*x) + 10
    plt.plot(x, y)
    plt.grid(True)
    plt.show()

#plot_func()

def quad_reg(x):
    return ((5000.002 + np.power((5000.002**2) - (4 * 1 * 10),0.5))/ (2 * 1)) - x

def quad_special(x):
    return ((-2 * 10)/(-5000.002 + np.power((5000.002**2) - (4 * 1 * 10), 0.5))) - x



#HERE IS MY ANSWER BERNIE
def hw_answer():

    quad_reg_answer1, it, err = bisection_method(quad_reg, 4000, 5500)
    quad_reg_answer2, it, err = bisection_method(quad_reg, -1000, 500)
    print(f'The roots of the regular quadratic equation with 5-digit chopping is: {quad_reg_answer1:.5f} and {quad_reg_answer2}')

    quad_spec_answer1, it, err = bisection_method(quad_special, 4500, 5200)
    quad_spec_answer2, it, err = bisection_method(quad_special, -500, 500)
    print(f'The roots of the special quadratic equation with 5-digit chopping is: {quad_spec_answer1:.5f} and {quad_spec_answer2}')

hw_answer()


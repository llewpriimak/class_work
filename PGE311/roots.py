import numpy as np
import matplotlib
import matplotlib.pyplot as plt



# Set of test functions
def f(c):
    #fc = (667.38 / c) * (1 - np.exp(-0.141684 * c)) - 40

    return ((4*np.arccos((2-c)/2)-(2-c)*np.sqrt(2*2*c-c**2))*5) - 62 #fc

#print(f())

def p(x):
    px = x**3 -5*x **2 + x +2.5
    return px

def f2(x):
    return x**4-x-10

def g(x):
    return x**4 + 10

def g1(x):
    return (x+10)**(1/4)

def dp(x):
    return 3*x**2 -10*x+1


# This function can find the root by using the bisection method
# This uses upper and lower bounds where xl is the lower bound and xu is the
# upper bound. f is the function to find the root on.
# Changing eps will change the error cutoff.
# Returns the root, the number of iterations, and the error.
def bisection_method(f, xl, xu, eps=0.0000005):

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
    print('The root approximation is', xm, 'The number of iterations:', it)
    return xm, it, err


# This function can be used to find the root using the false position method
# This uses upper and lower bounds where xl is the lower bound and xu is the
# upper bound. f is the function to find the root on.
# Changing eps will change the error cutoff.
# Returns the root, the number of iterations, and the error.
def false_position_method(f, xl, xu, eps=0.0125):

    # Initialize the function
    err = xu - xl
    it = 0
    max_it = 10000
    xm = (xl + xu) / 2

    # Execute the iterations
    while err > eps and it < max_it:
        xm = xu - (f(xu) * (xl - xu)) / (f(xl) - f(xu))
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
    print('The root approximation is', xm, 'The number of iterations:', it)
    return xm, it, err

xm,it,err = bisection_method(f,0,4)
print(xm)
print(it)
print(err)

# This function can be used to find the root using the fixed point method
# x0 represents the point to start the fixed point
# f is the function to find the root on.
# Changing eps will change the error cutoff.
# Returns the root, the number of iterations, and the error.
def fixed_point(f, x0, eps=0.0125):

    # Initialize the function
    x1 = g(x0)
    err = np.abs(x1 - x0)
    it = 0
    max_it = 5

    # Execute the iterations
    while err > eps and it < max_it:
        x1 = f(x0)
        err = np.abs(x1 - x0)
        x0 = x1
        it += 1

    return x1, it, err


# This function can be used to find the root using the newton method
# This requires using the slope, f is the function to find the root on
# and df is the derivative of that function that takes one argument
# Changing eps will change the error cutoff.
# Returns the root, the number of iterations, and the error.
def newton_method(f, df, x0, eps=0.001):

    # Initialize the function
    rel_err = 10 * eps
    it = 0
    max_it = 50000

    # Execute the iterations
    while rel_err > eps and it < max_it:

        x1 = x0 - f(x0) / df(x0)
        rel_err = np.abs(x1 - x0)
        if np.abs(x0) > eps:
            rel_err /= np.abs(x0)
        x0 = x1
        it += 1

    return x1, it, rel_err


#This function can be used to find the root using the secant method
# This requires finding the slope through two points. This is defined as
# x0 and x1.
# f is the function to find the root on.
# Changing eps will change the error cutoff.
# Returns the root, the number of iterations, and the error.
def secant_method(f, x0, x1, eps=0.001):

    # Initialize the function
    rel_err = 10 * eps
    it = 0
    max_it = 50000

    # Execute the iterations
    while rel_err > eps and it < max_it:

        # x1 = x0 - p(x0)/dp(x0)
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        rel_err = np.abs(x2 - x1)
        if np.abs(x1) > eps:
            rel_err /= np.abs(x1)
        x0 = x1
        x1 = x2
        it += 1


    return x1, it, rel_err
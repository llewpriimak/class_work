import numpy as np


# For part b, I changed the value that was subtracted to fill out
# the table of different volumes

def f(c):

    return ((4*np.arccos((2-c)/2)-(2-c)*np.sqrt(2*2*c-c**2))*5) - 62 #fc



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


xm,it,err = bisection_method(f,0,4)
print(xm)
print(it)
print(err)


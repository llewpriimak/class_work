import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

#Plotting function called by linear_regression()
def linear_plot(x,y,a0,a1):

    plt.xlabel('X'); plt.ylabel('Y')
    plt.plot(x, y, 'ro', label='Data points'); plt.plot(x, a0 + a1 * x, label='Fitting')
    e = y - np.exp(a0) - a1 * x
    mu = np.exp(a0)*np.exp(a1/x)
    # print(mu)
    # print(e)
    plt.plot(e,mu,'b*',label = 'Residuals')
    plt.grid(True)
    plt.legend()
    plt.show()


#Plotting function called by linear_regression()
def curve_plot(x,y,A0,B):

    A = np.exp(A0)
    plt.xlabel('log X'); plt.ylabel('log Y')
    plt.plot(x, y, 'ro', label='Data points')
    plt.plot(x, A * (x ** B),label='Fitting')
    plt.grid(True)
    plt.legend()
    plt.show()


#Plotting function called by polynomial_regression()
def poly_plot(x,y,a0,a1,a2):


    plt.xlabel('X'); plt.ylabel('Y')
    plt.plot(x, y, 'ro', label='Data points')
    plt.plot(x, a0+(a1*x)+(a2*np.power(x,2)),label='Fitting')
    plt.grid(True)
    plt.legend()
    plt.show()

# The linear_regression function is good for fitting a line through
# a set of data points. It can plot for both linear and logarithmic
# data sets
def linear_regression(x, y):
    n = len(x)

    what_type = 2#int(input('Type 2 for linear, type 1 for logarithmic: '))
    if what_type == 1:
        x = np.log(x)
        y = np.log(y)

    A = np.array([[n, np.sum(x)], [np.sum(x), np.sum(x ** 2)]])
    b = np.array([np.sum(y), np.sum(x * y)])

    answers = np.linalg.solve(A, b)
    # print(answers)
    a0 = answers[0]
    a1 = answers[1]


    plot_it = 1#int(input('Type 1 for plot, 0 for no plot: '))
    if what_type == 2 and plot_it == 1:
        linear_plot(x,y,a0,a1)

    elif plot_it == 1 and plot_it == 1:
        curve_plot(np.exp(x),np.exp(y),a0,a1)


    return a0,a1


# Polynomial regression function is good for plotting a polynomial line
# through a set of point. This is good for fitting with respect to curves
# bends in the data trend.
def polynomial_regression(x,y):

    n = len(x)
    A = np.array([[n, np.sum(x), np.sum(x**2)],
                  [np.sum(x),np.sum(x**2),np.sum(x**3)],
                  [np.sum(x**2),np.sum(x**3),np.sum(x**4)]])
    b = np.array([np.sum(y),np.sum(x*y),np.sum((x**2)*y)])

    a0,a1,a2 = np.linalg.solve(A,b)


    plot_it = int(input('Type 1 for poly_plot, 0 for no plot: '))
    if plot_it == 1:

        poly_plot(x,y,a0,a1,a2)


    return a0,a1,a2


def r2_calc(x,y):
    n = len(x)

    numerator = n*np.sum(x*y)-np.sum(x)*np.sum(y)
    denom = np.power(n*np.sum(x**2)-np.sum(x)**2,0.5)*np.power(n*np.sum(y**2)-np.sum(y)**2,0.5)
    r = numerator/denom
    r2 = np.power(r,2)
    return r2
x = np.array([26.67,93.33,148.89,315.56])
y = np.array([1.35,0.085,0.012,0.00075])
a0,a1 = linear_regression(x,np.log(y))
print('b0 is equal to:',np.exp(a0),'b1 is equal to: ',a1)
r2 = r2_calc(x,y)
print('r2 is equal to: ', r2)



#print(a0*np.exp(a1/26.67))
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

#Plotting function called by linear_regression()
def linear_plot(x,y,a0,a1):

    plt.xlabel('X'); plt.ylabel('Y')
    plt.plot(x, y, 'ro', label='Data points'); plt.plot(x, a0 + a1 * x, label='Fitting')
    # slope, int = np.polyfit(x,a0 + a1 * x,1)
    # print(slope)
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

    what_type = int(input('Type 2 for linear, type 1 for logarithmic: '))
    if what_type == 1:
        x = np.log(x)
        y = np.log(y)

    A = np.array([[n, np.sum(x)], [np.sum(x), np.sum(x ** 2)]])
    b = np.array([np.sum(y), np.sum(x * y)])

    answers = np.linalg.solve(A, b)
    # print(answers)
    a0 = answers[0]
    a1 = answers[1]

    plot_it = int(input('Type 1 for plot, 0 for no plot: '))
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



# x = np.array([2.5, 3.5, 5, 6, 7.5, 10, 12.5, 15, 17.5, 20])
# y = np.array([7, 5.5, 4.1, 3.9, 3.4, 3.9, 2.6, 2.4, 2.3, 2.1])
# x = np.array([0.156,0.23,0.312,0.390,0.468,0.546,0.624,0.702,0.780])
# y = np.array([3.326,2.217,1.663,1.330,1.109,0.950,0.831,0.739,0.665])
# x = np.array([4,8,12,16,20,24])
# y = np.array([1600,1320,1000,890,650,560])
# x1 = np.array([10,20,30,40,50,60,70,80])
# y1 = np.array([25,70,380,550,610,1220,830,1450])

# a0, a1 = linear_regression(x, np.log(y))
# a0 = np.exp(a0)
x = np.array([26.67,93.33,148.89,315.56])
y = np.array([1.35,0.085,0.012,0.00075])
a0,a1 = linear_regression(x,np.log(y))
print('b0 is equal to:',np.exp(a0),'b1 is equal to: ',a1)
#Question 5 answer 1985.4366, -0.05350634
# A0,B = linear_regression(x,y)
# a0,a1,a2 = polynomial_regression(x1,y1)



print(a0*np.exp(a1/26.67))
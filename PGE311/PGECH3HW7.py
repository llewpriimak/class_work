import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt

def lettergrade(score):


    if score >= 90 and score <= 100:
        return 'A'
    elif score >= 80 and score <= 90:
        return 'B'
    elif score >= 70 and score <= 80:
        return 'C'
    elif score >= 60 and score <= 70:
        return 'D'
    elif score >= 0 and score <= 60:
        return 'F'
    else:
        print('Invalid score')

lettergrade(90)


def cyltank(r,L,plot_title):

    h = np.linspace(0, 2*r, 100)
    volume = (np.power(r, 2)*np.arccos((r-h)/r)-(r-h)*np.power(2*r*h-h**2,0.5)) * L

    plt.xlabel('liquid volume')
    plt.ylabel('depth')
    plt.grid(True)
    plt.title(plot_title)
    plt.plot(volume, h)
    plt.show()

#cyltank(3,5,'Volume vs.Depth for Horizontal Cylindrical Tank')
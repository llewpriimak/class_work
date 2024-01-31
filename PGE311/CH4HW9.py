import math
import numpy as np

##function that acts as the maclaurin series

def itermeth(x, es = 1e-4, maxit = 10):
    iter = 1
    sol = 1
    ea = 100
    while True:
        solold = sol
        sol = (sol + (x/sol)) /2
        iter = iter + 1
        if sol !=0: ea = abs((sol-solold)/sol) * 100
        if ea < es or iter == maxit: break
        fx = sol

    return fx, ea, iter

itermeth(50)
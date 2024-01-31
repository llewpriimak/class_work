import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from Line_fitting import *



V = np.array([0.156,0.23,0.312,0.390,0.468,0.546,0.624,0.702,0.780])
P = np.array([3.326,2.217,1.663,1.330,1.109,0.950,0.831,0.739,0.665])
n = 10/64.07
R = 8.3145*(10**-3)
T = 400
z = np.linspace(0,1,500)
# linear_regression(1/V,P)
plt.plot(1/V,(n*R*T)/V); plt.xlabel('1/V'); plt.ylabel('(n*R*T)/V');plt.title('Predicted pressure by ideal gas law')
plt.grid(True)
plt.show()

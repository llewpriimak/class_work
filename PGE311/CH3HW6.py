import numpy as np
import math

apr = 5.3
p = 55000
i = (apr / 100) / 12
for n in range(0, 73, 12):
    a = p * ((i * (np.power(1 + i, n))) / (np.power(1 + i, n) - 1))
    print(f'months {n}')
    print(f'Payment {a}')




# z = 1
# x = 0.9
# y = 0
# for i in range(1,16, 2):
#
#     if z == 0:
#         y -= np.power(x,i)/math.factorial(i)
#         z = 1
#     else:
#         y += np.power(x, i) / math.factorial(i)
#         z = 0
#
# error  = (np.sin(0.9) - y)/np.sin(0.9) * 100
# print(y)


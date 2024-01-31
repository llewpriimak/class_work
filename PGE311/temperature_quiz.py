import numpy as np
import matplotlib.pyplot as plt

my_file = open('Temperature.txt', 'r')
firstline = my_file.readline()

data = np.fromfile(my_file, dtype = float, count = 12*4, sep = " ")
my_file.close()

data.shape = (12,4)
plt.xlabel('Month')
plt.ylabel('Temperature(F)')
plt.plot(data[:,0], data[:,1], 'rd' , label = 'high')
plt.plot(data[:,0], data[:,2], 'bo' , label = 'low')
plt.plot(data[:,0], data[:,3], 'gx' , label = 'ave')

plt.legend()
# plt.show()
plt.savefig('PlotAssignment.pdf')
print(data)
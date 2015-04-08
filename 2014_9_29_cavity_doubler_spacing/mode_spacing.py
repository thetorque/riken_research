import numpy as np
from matplotlib import pyplot
import matplotlib

## plot data of c parameters

#data124 = stage A gain#
cavity_scan = np.loadtxt(open("CH1.csv",'rb'),delimiter=' ')
time = np.linspace(-0.03360,0.01638,np.size(cavity_scan))


pyplot.plot(time,cavity_scan)
 
 
## control the size of the plot
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6,4)
 
pyplot.show()

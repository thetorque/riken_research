import numpy as np
from matplotlib import pyplot
import matplotlib

## plot data of c parameters

#spectrum_low_gain#

freq = np.loadtxt(open("spectrum_freq.csv"))
A = np.loadtxt(open("spectrum_A.csv"))
B = np.loadtxt(open("spectrum_B.csv"))
C = np.loadtxt(open("spectrum_C.csv"))

 
## plot all responses ##
freq = freq/1000000.0
pyplot.plot(freq,A)
pyplot.plot(freq,B)
pyplot.plot(freq,C)

pyplot.xlim([np.min(freq),np.max(freq)])
 
 
## control the size of the plot
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6,4)
 
pyplot.show()

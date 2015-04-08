import numpy as np
from matplotlib import pyplot
import matplotlib

## plot data of c parameters

#data124 = stage A gain#
spectrum_opt = np.loadtxt(open("average.csv"))
spectrum_max_gain = np.loadtxt(open("max_gain.csv"))
freq = np.loadtxt(open("freq.csv"))/1000000-20

print spectrum_opt

pyplot.plot(freq,spectrum_opt)
#pyplot.plot(freq,spectrum_max_gain)
  
  
## control the size of the plot
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6,4)
  
pyplot.show()

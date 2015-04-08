import numpy as np
from matplotlib import pyplot
import matplotlib

## plot data of c parameters

#data132 = stage C gain#
data132 = np.loadtxt(open("132.csv",'rb'),delimiter=',',skiprows=1)
freq_array = data132[:,0]
stage_C1_gain_array = 10*np.log(data132[:,1])

#data134 = stage C gain#
data134 = np.loadtxt(open("134.csv",'rb'),delimiter=',',skiprows=1)
stage_C2_gain_array = 10*np.log(data134[:,1])




## plot all responses ##
pyplot.plot(freq_array,stage_C1_gain_array)
pyplot.plot(freq_array,stage_C2_gain_array)

## change to log scale (y scale already in dB###
pyplot.xscale('log',basey = 10,subsy=[2, 3, 4, 5, 6, 7, 8, 9])
pyplot.xlim([50,5000000])

## control the size of the plot
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6,4)

pyplot.show()

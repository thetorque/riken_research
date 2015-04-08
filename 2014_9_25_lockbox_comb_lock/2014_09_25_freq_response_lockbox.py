import numpy as np
from matplotlib import pyplot
import matplotlib

## plot data of c parameters

#data124 = stage A gain#
data124 = np.loadtxt(open("124.csv",'rb'),delimiter=',',skiprows=1)
freq_array = data124[:,0]
stage_A_gain_array = 10*np.log(data124[:,1])

#data126 = stage AB gain#
data126 = np.loadtxt(open("126.csv",'rb'),delimiter=',',skiprows=1)
stage_AB_gain_array = 10*np.log(data126[:,1])

#data134 = stage C gain#
data134 = np.loadtxt(open("134.csv",'rb'),delimiter=',',skiprows=1)
stage_C_gain_array = 10*np.log(data134[:,1])

#data136 = stage ABC gain#
data136 = np.loadtxt(open("136.csv",'rb'),delimiter=',',skiprows=1)
stage_ABC_gain_array = 10*np.log(data136[:,1])


## plot all responses ##
pyplot.plot(freq_array,stage_A_gain_array)
pyplot.plot(freq_array,stage_AB_gain_array)
pyplot.plot(freq_array,stage_ABC_gain_array)
pyplot.plot(freq_array,stage_C_gain_array)

## change to log scale (y scale already in dB###
pyplot.xscale('log',basey = 10,subsy=[2, 3, 4, 5, 6, 7, 8, 9])
pyplot.xlim([50,5000000])

## control the size of the plot
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6,4)

pyplot.show()

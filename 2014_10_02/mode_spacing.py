import numpy as np
from matplotlib import pyplot
import matplotlib

## plot data of c parameters

#data124 = stage A gain#
ch1_810 = np.loadtxt(open("810_ch1.csv",'rb'))
ch2_810 = np.loadtxt(open("810_ch2.csv",'rb'))
time_810 = np.loadtxt(open("810_time.csv",'rb'))

ch1_870 = np.loadtxt(open("870_ch1.csv",'rb'))
ch2_870 = np.loadtxt(open("870_ch2.csv",'rb'))
time_870 = np.loadtxt(open("870_time.csv",'rb'))


pyplot.plot(time_810,ch1_810)
#pyplot.plot(time_870,ch1_870)
#pyplot.plot(time_810,ch2_810)
#pyplot.plot(time_870,ch2_870)
 

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6,4)
 
pyplot.show()

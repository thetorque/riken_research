import numpy as np
from matplotlib import pyplot
import matplotlib

## plot data of c parameters

#data124 = stage A gain#
ch1_810 = np.loadtxt(open("810NEWER_CH1.csv",'rb'))
ch1_810_old = np.loadtxt(open("810NEW_CH1.csv",'rb'))
ch2_810 = np.loadtxt(open("810NEWER_CH2.csv",'rb'))
time_810 = np.loadtxt(open("810NEWER_time.csv",'rb'))


pyplot.plot(time_810,ch1_810)
#pyplot.plot(time_810,ch1_810_old)
#pyplot.plot(time_870,ch1_870)
#pyplot.plot(time_810,ch2_810/3000)
#pyplot.plot(time_870,ch2_870)
 

fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6,4)
 
pyplot.show()

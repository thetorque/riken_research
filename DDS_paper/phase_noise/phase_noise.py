from __future__ import division
import numpy as np
from matplotlib import pyplot
import matplotlib
import lmfit


#data132 = stage C gain#
ref = np.loadtxt('2GHz_clock.csv',delimiter=',',skiprows=53)
ref2 = np.loadtxt('10mhzclock.csv',delimiter=',',skiprows=53)
data1 = np.loadtxt('trace1_123 MHZ.csv',delimiter=',',skiprows=53)
data2 = np.loadtxt('trace1_345MHZ.csv',delimiter=',',skiprows=53)
data3 = np.loadtxt('trace_51MHz.csv',delimiter=',',skiprows=53)



pyplot.xscale('log',basex = 10,subsy=[2, 3, 4, 5, 6, 7, 8, 9])
xtick_position = [10,100,1000,10000,100000,1000000,10000000,100000000]
xtick_label = [10,100,'1k','10k','100k','1M','10M','100M']
pyplot.xticks(xtick_position,xtick_label)
pyplot.grid(True, which='both', color='#DDE4DD', linestyle='-', linewidth=0.5,zorder=-1)
#pyplot.yscale('log',basey = 10,subsy=[2, 3, 4, 5, 6, 7, 8, 9])

pyplot.plot(ref[:,0],ref[:,1],zorder=3,linewidth=2.0) ## plot reference
pyplot.plot(ref2[:,0],ref2[:,1],zorder=3,linewidth=2.0) ## plot reference
#pyplot.plot(data1[:,0],data1[:,1],zorder=3,linewidth=2.0) ## plot 123 MHz
#pyplot.plot(data2[:,0],data2[:,1],zorder=3,linewidth=2.0) ## plot 345 MHz
#pyplot.plot(data3[:,0],data3[:,1],zorder=3,linewidth=2.0) ## plot 51 MHz
pyplot.show()
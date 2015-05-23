from __future__ import division
import numpy as np
from matplotlib import pyplot
import matplotlib
import lmfit


#data132 = stage C gain#
# ref = np.loadtxt('2GHz_clock.csv',delimiter=',',skiprows=53)
# ref2 = np.loadtxt('10mhzclock.csv',delimiter=',',skiprows=53)
# data1 = np.loadtxt('trace1_123 MHZ.csv',delimiter=',',skiprows=53)
# data2 = np.loadtxt('trace1_345MHZ.csv',delimiter=',',skiprows=53)
# data3 = np.loadtxt('trace_51MHz.csv',delimiter=',',skiprows=53)


## before
freq = np.array([0.05,0.06,0.07,0.08,0.09,0.1,0.2,0.5,1,2,5,10,20,50,100,200])
amp = np.array([-10.8,-7.4,-5.0,-3.4,-2.4,-1.45,0.9,1.8,1.99,2.31,2.52,2.40,2.15,1.33,0.18,-1.50])

##after
freq2 = np.array([0.05,0.06,0.07,0.08,0.09,0.1,0.2,0.5,1,2,5,10,20,50,100,200,300,350,375,390,395,400])
amp2 = np.array([-0.26,2.05,3.6,4.7,5.56,6.2,9.07,10.19,10.74,11.20,11.50,11.50,11.38,10.77,10.00,8.67,7.00,6.61,5.13,2.3,-0.2,-3.6])

## full range no filter
data = np.array([[0.0,-58],
                 [0.1,-55.7],
                 [0.2,-51.9],
                 [0.3,-47.7],
                 [0.4,-43.3],
                 [0.5,-38.7],
                 [0.6,-34.0],
                 [0.7,-29.2],
                 [0.8,-24.35],
                 [0.9,-19.44],
                 [1.0,-14.57],
                 [1.1,-9.58],
                 [1.2,-4.70],
                 [1.3,-1.28],
                 [1.32,-1.22],
                 [1.4,-1.62]
                 ])

data2 = np.array([[0.0,-56],
                 [0.1,-54],
                 [0.2,-50],
                 [0.3,-46],
                 [0.4,-41.6],
                 [0.5,-37],
                 [0.6,-32],
                 [0.7,-27.5],
                 [0.8,-22.6],
                 [0.9,-17.6],
                 [1.0,-12.8],
                 [1.1,-7.85],
                 [1.2,-2.89],
                 [1.3,1.02],
                 [1.4,2.42]
                 ])


#pyplot.xscale('log',basex = 10,subsy=[2, 3, 4, 5, 6, 7, 8, 9])
#xtick_position = [10,100,1000,10000,100000,1E6,1E7,1E8,8E8]
#xtick_label = [10,100,'1k','10k','100k','1M','10M','100M','800M']
#pyplot.xticks(xtick_position,xtick_label)
pyplot.grid(True, which='both', color='#DDE4DD', linestyle='-', linewidth=0.5,zorder=-1)
#pyplot.yscale('log',basey = 10,subsy=[2, 3, 4, 5, 6, 7, 8, 9])

#pyplot.plot(freq,amp,zorder=3,linewidth=2.0) ## plot reference
#pyplot.plot(freq2,amp2,zorder=3,linewidth=2.0) ## plot reference

pyplot.plot(data[:,0],data[:,1]+20,zorder=3,linewidth=2.0)
pyplot.plot(data2[:,0],data2[:,1]+20,zorder=3,linewidth=2.0)


#pyplot.plot(ref2[:,0],ref2[:,1],zorder=3,linewidth=2.0) ## plot reference
#pyplot.plot(data1[:,0],data1[:,1],zorder=3,linewidth=2.0) ## plot 123 MHz
#pyplot.plot(data2[:,0],data2[:,1],zorder=3,linewidth=2.0) ## plot 345 MHz
#pyplot.plot(data3[:,0],data3[:,1],zorder=3,linewidth=2.0) ## plot 51 MHz
pyplot.show()
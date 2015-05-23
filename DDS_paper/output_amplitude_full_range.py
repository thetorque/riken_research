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
data = np.array([[0.01,-26.53],
                 [0.02,-20.27],
                 [0.03,-16.98],
                 [0.04,-14.33],
                 [0.05,-12.50],
                 [0.06,-10.98],
                 [0.07,-9.73],
                 [0.08,-8.67],
                 [0.09,-7.76],
                 [0.1,-6.97],
                 [0.2,-3.43],
                 [0.3,-3.16],
                 [0.4,-3.08],
                 [0.5,-2.91],
                 [0.6,-2.83],
                 [0.7,-2.76],
                 [0.8,-2.7],
                 [0.9,-2.65],
                 [1.0,-2.60],
                 [2.0,-2.32],
                 [3.0,-2.16],
                 [4.0,-2.07],
                 [5.0,-2.03],
                 [6.0,-2.00],
                 [7.0,-1.97],
                 [8.0,-1.94],
                 [9.0,-1.95],
                 [10.0,-1.95],
                 [20.0,-1.98],
                 [30.0,-2.08],
                 [40.0,-2.15],
                 [50.0,-2.19],
                 [60.0,-2.19],
                 [70.0,-2.22],
                 [80.0,-2.27],
                 [90.0,-2.33],
                 [100.0,-2.40],
                 [200.0,-3.45],
                 [300.0,-4.90],
                 [400.0,-7.44],
                 [500.0,-10.20],
                 [600.0,-12.86],
                 [700.0,-14.36],
                 [800.0,-15.88]
                 ])


## full range no filter V=1.4

data2 = np.array([[0.1,-7.43],
                 [0.2,-2.23],
                 [0.3,-0.1],
                 [0.4,0.27],
                 [0.5,0.53],
                 [0.6,0.70],
                 [0.7,0.82],
                 [0.8,0.92],
                 [0.9,1.00],
                 [1.0,1.09],
                 [2.0,1.37],
                 [3.0,2.30],
                 [4.0,2.52],
                 [5.0,2.52],
                 [6.0,2.47],
                 [7.0,2.42],
                 [8.0,2.35],
                 [9.0,2.20],
                 [10.0,2.10],
                 [20.0,1.59],
                 [30.0,1.37],
                 [40.0,1.18],
                 [50.0,1.11],
                 [60.0,1.07],
                 [70.0,1.00],
                 [80.0,0.92],
                 [90.0,0.78],
                 [100.0,0.66],
                 [150.0,-1.50],
                 [200.0,-1.56],
                 [250.0,-0.75],
                 [300.0,-0.60],
                 [350.0,-1.11],
                 [400.0,-1.76]
                 ])


pyplot.xscale('log',basex = 10,subsy=[2, 3, 4, 5, 6, 7, 8, 9])
xtick_position = [10,100,1000,10000,100000,1E6,1E7,1E8,8E8]
xtick_label = [10,100,'1k','10k','100k','1M','10M','100M','800M']
pyplot.xticks(xtick_position,xtick_label)
pyplot.grid(True, which='both', color='#DDE4DD', linestyle='-', linewidth=0.5,zorder=-1)
#pyplot.yscale('log',basey = 10,subsy=[2, 3, 4, 5, 6, 7, 8, 9])

#pyplot.plot(freq,amp,zorder=3,linewidth=2.0) ## plot reference
#pyplot.plot(freq2,amp2,zorder=3,linewidth=2.0) ## plot reference

pyplot.plot(data[:,0]*1000000,data[:,1]+20,zorder=3,linewidth=2.0)
pyplot.plot(data2[:,0]*1000000,data2[:,1]+20,zorder=3,linewidth=2.0)


#pyplot.plot(ref2[:,0],ref2[:,1],zorder=3,linewidth=2.0) ## plot reference
#pyplot.plot(data1[:,0],data1[:,1],zorder=3,linewidth=2.0) ## plot 123 MHz
#pyplot.plot(data2[:,0],data2[:,1],zorder=3,linewidth=2.0) ## plot 345 MHz
#pyplot.plot(data3[:,0],data3[:,1],zorder=3,linewidth=2.0) ## plot 51 MHz
pyplot.show()
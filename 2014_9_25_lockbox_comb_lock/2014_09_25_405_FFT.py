import numpy as np
from matplotlib import pyplot
import matplotlib

## plot data of c parameters

#spectrum_low_gain#

data1 = np.loadtxt(open("blkMem009.txt"),delimiter=',',skiprows=16)
data2 = np.loadtxt(open("blkMem008.txt"),delimiter=',',skiprows=16)

data3 = np.loadtxt(open("blkMem007.txt"),delimiter=',',skiprows=16)
data4 = np.loadtxt(open("blkMem006.txt"),delimiter=',',skiprows=16)

## smoothening of the data ##

y1 = data1[:,1]
y_avg1 = (y1[:-4]+y1[1:-3]+y1[2:-2]+y1[3:-1]+y1[4:])/5
freq1 = data1[:,0][2:-2]

y2 = data2[:,1]
y_avg2 = (y2[:-4]+y2[1:-3]+y2[2:-2]+y2[3:-1]+y2[4:])/5
freq2 = data2[:,0][2:-2]

y3 = data3[:,1]
y_avg3 = (y3[:-4]+y3[1:-3]+y3[2:-2]+y3[3:-1]+y3[4:])/5
freq3 = data3[:,0][2:-2]

y4 = data4[:,1]
y_avg4 = (y4[:-4]+y4[1:-3]+y4[2:-2]+y4[3:-1]+y4[4:])/5
freq4 = data4[:,0][2:-2]
 
## plot all responses ##


cut_off = 30


pyplot.plot(freq1[cut_off:],y_avg1[cut_off:],color='blue')
pyplot.plot(freq2[cut_off:],y_avg2[cut_off:],color = 'black')
pyplot.plot(freq3,y_avg3,color='blue')
pyplot.plot(freq4,y_avg4,color = 'black')

pyplot.xscale('log',basey = 10,subsy=[2, 3, 4, 5, 6, 7, 8, 9])
 
pyplot.xlim([np.min(freq3),np.max(freq1)])
  
  
## control the size of the plot
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6,4)
  
pyplot.show()

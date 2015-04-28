from __future__ import division
import numpy as np
from matplotlib import pyplot
import matplotlib
import lmfit



ch1 = np.loadtxt("ALL0000/trace1.CSV") ## TTL on a different channel
ch2 = np.loadtxt("ALL0000/trace2.CSV") ## switch RF from completely off state
ch3 = np.loadtxt("ALL0001/trace2.CSV") ## switch RF from low power to high power
ch4 = np.loadtxt("ALL0003/trace2.CSV")[700:] ## switch frequency
ch4_pulse = np.loadtxt("ALL0003/trace1.CSV")[600:] ## switch frequency pulse



## scale up the voltage for channel 2
ch2[:,1] = ch2[:,1]*50+6
ch3[:,1] = ch3[:,1]*50+12
ch4[:,1] = ch4[:,1]*50+18

## time scaling
ch4_pulse[:,0] = ch4_pulse[:,0]*1000000
ch4[:,0] = ch4[:,0]*1000000
ch3[:,0] = ch3[:,0]*1000000
ch2[:,0] = ch2[:,0]*1000000
ch1[:,0] = ch1[:,0]*1000000

#pyplot.plot(ch1[:,0], ch1[:,1])
pyplot.plot(ch2[:,0], ch2[:,1], linewidth=2.0)
pyplot.plot(ch3[:,0], ch3[:,1], linewidth=2.0)
pyplot.plot(ch4[:,0], ch4[:,1], linewidth=2.0)
pyplot.plot(ch4_pulse[:,0], ch4_pulse[:,1], linewidth=2.0)

## set grid
pyplot.grid(True, which='both')

## set plot limit
pyplot.xlim([-0.1,1.2])
pyplot.ylim([-1.0,22])

pyplot.show()
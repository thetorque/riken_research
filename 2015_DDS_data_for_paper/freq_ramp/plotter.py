from __future__ import division
import numpy as np
from matplotlib import pyplot
import matplotlib
import lmfit



ch1 = np.loadtxt("RefCurve_2015-04-22_1_180600.Wfm.csv", delimiter=";") [0:100000]## 



rf_0 = ch1[:,0]+0.15
rf_1 = ch1[:,1]+0.26
pulse = ch1[:,2]*0.2

time = np.arange(np.size(rf_0))*2e-3

pyplot.plot(time,rf_0, linewidth=2.0)
pyplot.plot(time,rf_1, linewidth=2.0)
pyplot.plot(time,pulse, linewidth=2.0)

## set grid
pyplot.grid(True, which='both')

## set plot limit
#pyplot.xlim([-0.1,2.1])
#pyplot.ylim([-0.01,0.4])

pyplot.show()
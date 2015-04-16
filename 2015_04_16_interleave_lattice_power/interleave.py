from __future__ import division
import numpy as np
from matplotlib import pyplot
import matplotlib
import lmfit


#data132 = stage C gain#
#wave = np.loadtxt(open("150415203929stab.csv",'rb'),delimiter=' ', skiprows=1)
wave = np.loadtxt("150415203929stab.csv",skiprows=3)
wave_cut = np.loadtxt("150415203929stab_cut.csv",skiprows=3)


center_freq = wave_cut[:,1]
time_stamp = wave_cut[:,3]-wave_cut[:,3][0]

S_state = wave_cut[:,4]
P_state = wave_cut[:,5]
N_atom = wave_cut[:,6]

#pyplot.plot(wave_cut[:,4])
#pyplot.plot(wave_cut[:,5])
#pyplot.plot(wave_cut[:,6])
pyplot.plot(wave_cut[:,7])
pyplot.show()
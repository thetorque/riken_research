from __future__ import division
import numpy as np
from matplotlib import pyplot
import matplotlib
import lmfit


#data132 = stage C gain#
wave = np.loadtxt(open("DDS_wave_form.csv",'rb'),delimiter=';')
wave = wave[200000:400000]

pyplot.plot(wave[:,1])
pyplot.show()
from __future__ import division
import numpy as np
from matplotlib import pyplot
import matplotlib
import lmfit


#data132 = stage C gain#
wave = np.loadtxt("DataLogA_20150430_074908.csv")
data1 = wave[2:119] - np.average(wave[2:119])
data1 = data1*1000
time1 = np.arange(np.size(data1))
data2 = wave[159:279]- np.average(wave[2:119])
data2 = data2*1000
time2 = np.arange(np.size(data2)) + time1[-1]
data3 = wave[319:440]- np.average(wave[2:119])
data3 = data3*1000
time3 = np.arange(np.size(data3)) + time2[-1]
data4 = wave[459:595]- np.average(wave[2:119])
data4 = data4*1000
time4 = np.arange(np.size(data4)) + time3[-1]
#wave = wave[200000:400000]


##15.22535454300 MHz


pyplot.plot(time1,data1, color = 'blue')
pyplot.plot(time1,np.ones_like(time1)*np.average(data1), color = 'black', linewidth = 3.0)
print "average =", np.average(data1), " pm ", np.std(data1)/np.sqrt(np.size(data1)-1)
pyplot.plot(time2,data2, color = 'blue')
pyplot.plot(time2,np.ones_like(time2)*np.average(data2), color = 'black', linewidth = 3.0)
print "average =", np.average(data2), " pm ", np.std(data2)/np.sqrt(np.size(data2)-1)
pyplot.plot(time3,data3, color = 'blue')
pyplot.plot(time3,np.ones_like(time3)*np.average(data3), color = 'black', linewidth = 3.0)
print "average =", np.average(data3), " pm ", np.std(data3)/np.sqrt(np.size(data3)-1)
pyplot.plot(time4,data4, color = 'blue')
pyplot.plot(time4,np.ones_like(time4)*np.average(data4), color = 'black', linewidth = 3.0)
print "average =", np.average(data4), " pm ", np.std(data4)/np.sqrt(np.size(data4)-1)
pyplot.show()
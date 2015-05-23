from __future__ import division
import labrad
import numpy as np
from matplotlib import pyplot
import matplotlib
import lmfit

def allan_model(params, x):
    A = params['A'].value
    B = params['B'].value
    output = A/np.power(x,B)
    #output = A/(x**B)
    return output
'''
define how to compare data to the function
'''
def allan_fit(params , x, data, err):
    model = allan_model(params, x)
    return (model - data)/err



Hg = np.loadtxt("150522195817stab.dat",skiprows=3)
excitation_rate = Hg[:,21]
number = Hg[:,0]
error_1 = Hg[:,13]
error_2 = Hg[:,14]

number = number%3
error_signal_1 = error_1[np.where(number == 1.0)]
error_signal_2 = error_2[np.where(number == 1.0)]

raman_1 = error_signal_1[160:251]
print np.std(raman_1)
raman_2 = error_signal_2[160:251]
print np.std(raman_2)
ecdl_1 = error_signal_1[280:450]
print np.std(ecdl_1)
ecdl_2 = error_signal_2[280:450]
print np.std(ecdl_2)

#pyplot.plot(ecdl_2)
#pyplot.plot(raman_2)
#pyplot.plot(error_signal_2)
#pyplot.plot(excitation_rate) #1008/2 = 252 ## 1040/4 = 260

#print number

#pyplot.plot(Hg[:,0],Hg[:,21]) ## excitation rate both channel
#pyplot.grid(True, which='both')

#pyplot.plot(Hg[:,0],Hg[:,9]) ## drift rate?
#pyplot.plot(Hg[:,0],Hg[:,13]) ## error signal? A
#pyplot.plot(Hg[:,0],Hg[:,14]) ## error signal? B

pyplot.show()

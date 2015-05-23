from __future__ import division
#import labrad
import numpy as np
from matplotlib import pyplot
import matplotlib
#import lmfit

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

ratio = 2.62931420989890960

Sr_time_offset = 43887229.263617
Hg_time_offset = 3512987633.790

Hg = np.loadtxt("150522195817stab.dat",skiprows=3)
#Hg_raw_time = Hg[:,3]-Hg[:,3][-1]
#Hg_raw_time = Hg[:,3]-Hg_time_offset
#Hg_freq = Hg[:,1]-Hg[:,1][-1]
#Sr_raw_freq = Sr[]

#Hg[:,7] excitation rate
#Hg[:,8] in loop +
#Hg[:,9] in loop -
pyplot.plot(Hg[:,0],Hg[:,21]) ## excitation rate
#pyplot.plot(Hg[:,0],Hg[:,14])

pyplot.show()

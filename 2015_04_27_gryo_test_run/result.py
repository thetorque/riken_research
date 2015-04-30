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

data = (np.array([0.570647,0.570599])-0.570647)*100000
temp = np.array([1,2])
err = np.array([0.000015,0.000047])*100000
pyplot.errorbar(temp,data,err,fmt='o',markersize = 10.0)
#  
#  
# pyplot.ylim([0.01,0.5])
# pyplot.xlim([50,35000])

pyplot.show()

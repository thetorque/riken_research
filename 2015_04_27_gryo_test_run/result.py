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

# 0.570647(15)


### 9.5 B-field
data = np.array([0.570662970575,0.570663572921,0.570674806672,0.570653218984,0.570645956019])
temp = np.array([1,2,3,4,7])
err = np.array([0.000018,0.000016,0.0000146,0.00000887,0.000012])
pyplot.errorbar(temp,data,err,fmt='o',markersize = 10.0)

### 5.5 B-field (first two) next one is 9.5 V

data2 = np.array([0.570674757931,0.570663417094])
temp2 = np.array([5,6])
err2 = np.array([0.000019,0.00002])
pyplot.errorbar(temp2,data2,err2,fmt='o',markersize = 10.0)

pyplot.errorbar([0,-1],[0.570647,0.570598],[0.000015,0.00024],fmt='o',markersize = 10.0)

#pyplot.errorbar([-2],[0.568385],[0.00012],fmt='o',markersize = 10.0)


## calculate weighted average

data = np.append(data,data2)
err = np.append(err,err2)

result = np.sum(data/err**2)/np.sum(1/err**2)
err = np.sqrt(1/np.sum(1/err**2))

result_x = np.linspace(-1.5, 7.5, 1000)
result_y = np.ones_like(result_x)*result
error_1 = np.ones_like(result_x)*result + err
error_2 = np.ones_like(result_x)*result - err
pyplot.plot(result_x,result_y)
pyplot.fill_between(result_x, error_2, error_1,color = 'gray')
print result, err

#  
#  
# pyplot.ylim([0.01,0.5])
# pyplot.xlim([50,35000])

pyplot.show()

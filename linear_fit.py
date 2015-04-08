import numpy as np
import lmfit
from matplotlib import pyplot
import labrad

'This is a fit of narrow line spectrum of the carrier'

'''
define the function
'''
def linear_model(params, x):
    A = params['A'].value
    B = params['B'].value
    model =  B + A * x
    return model
'''
define how to compare data to the function
'''
def linear_fit(params , x, data):
    model = linear_model(params, x)
    return (model - data)


power = np.array([1.4,4.3,7.0,8.8,12.0,15.7,17.8,20.2,24.4])
current = np.array([39.59,42.16,45.33,47.80,50.36,53.86,56.15,57.89,62.26])

power2 = np.array([22,18.5,14.2,9.9,5.4,2.0,1.1,0.5,1.1])
current2 = np.array([62.27,57.05,52.95,48.82,45.04,41.55,37.23,32.11,28.47])

x_data = current
y_data = power

x_data2 = current2
y_data2 = power2

'''
define the fitting parameters, with initial guesses. 
Here can also specify if some parameters are fixed, and the range of allowed values
'''
params = lmfit.Parameters()
params.add('A', value = 2000)
params.add('B', value = 0)
'''
run the fitting
'''
result = lmfit.minimize(linear_fit, params, args = (x_data, y_data))
'''
plot the result
'''
fit_values  = y_data + result.residual
x_fitted = np.arange(np.min(x_data)-5,np.max(x_data),0.1)
y_fitted = linear_model(params,x_fitted)
pyplot.plot(x_fitted, y_fitted, 'r', label = 'fitted',linewidth=3.0)
'''
plot the data
'''

#pyplot.plot((x_data-params['center'].value)*1000, y_data, 'o', markersize = 8.0, label = 'data')

'''
print out fitting summary
'''
lmfit.report_errors(params)
pyplot.tick_params(axis='both', which='major', labelsize=20)
#pyplot.legend()
pyplot.plot(x_data,y_data,'o')
#pyplot.plot(x_data2,y_data2,'o')
pyplot.xlim([0,65])
pyplot.ylim([0,26])
pyplot.show()
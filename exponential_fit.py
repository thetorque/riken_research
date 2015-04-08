import numpy as np
import lmfit
from matplotlib import pyplot
import labrad

'This is a fit of narrow line spectrum of the carrier'

'''
define the function
'''
def expo_model(params, x):
    A = params['A'].value
    B = params['B'].value
    tau = params['tau'].value
    model =  B + A * np.exp(-(x/tau))
    return model
'''
define how to compare data to the function
'''
def expo_fit(params , x, data, err):
    model = expo_model(params, x)
    return (model - data)/err


#time = np.array([50,100,150,200,250,300])
time = np.array([50,75,100,150,200,250,300])
#atoms = np.array([2079,1674,1375,1200,960,902])
#atoms = np.array([2632,2230,1906,1536,1359,1152])
#atoms = np.array([1158,867,718,597,455,348])
atoms = np.array([4327,3825,3340,2908,2342,1940,1673])
#atoms_err = np.array([38,40,31,20,17,16])
atoms_err = np.array([10,10,10,10,10,10,10])

x_data = time
y_data = atoms
y_err = atoms_err

'''
define the fitting parameters, with initial guesses. 
Here can also specify if some parameters are fixed, and the range of allowed values
'''
params = lmfit.Parameters()
params.add('A', value = 2000)
params.add('B', value = 0, vary = False)
params.add('tau', value = 100)
'''
run the fitting
'''
result = lmfit.minimize(expo_fit, params, args = (x_data, y_data, y_err))
'''
plot the result
'''
fit_values  = y_data + result.residual
x_fitted = np.arange(np.min(x_data),np.max(x_data),1)
y_fitted = expo_model(params,x_fitted)
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
pyplot.errorbar(x_data,y_data,y_err,fmt='o')
pyplot.xlim([0,350])
pyplot.ylim([0,6000])
pyplot.show()
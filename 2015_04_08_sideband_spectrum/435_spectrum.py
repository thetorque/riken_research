from __future__ import division
import numpy as np
from matplotlib import pyplot
import matplotlib
import lmfit


'''
define the function
'''
def lorentzian_model(params, x):
    area = params['area'].value
    linewidth = params['linewidth'].value
    center = params['center'].value
    model =  (area / np.pi) * (linewidth / 2.0)**2 / ( ((linewidth / 2.0)**2) + (x - center)**2  )
    return model
'''
define how to compare data to the function
'''
def lorentzian_fit(params , x, data):
    model = lorentzian_model(params, x)
    return model - data

## plot data of c parameters

#data132 = stage C gain#
V_09 = np.loadtxt("150408175747NofAtoms.dat",skiprows=3)
V_11 = np.loadtxt("150408180132NofAtoms.dat",skiprows=3)
V_13 = np.loadtxt("150408180533NofAtoms.dat",skiprows=3)
V_07 = np.loadtxt("150408181110NofAtoms.dat",skiprows=3)

spectrum = np.loadtxt("150408185131NofAtoms.dat",skiprows=3)
full_spectrum = spectrum[:,4]
spectrum1 = spectrum[:,4][193:232]-0.17

y_data = spectrum1
x_data = np.arange(np.size(y_data))*0.2-3.5913


'''
define the fitting parameters, with initial guesses. 
Here can also specify if some parameters are fixed, and the range of allowed values
'''
params = lmfit.Parameters()
params.add('area', value = 0.1, max=2.0)
params.add('center', value = 28.27)
params.add('linewidth', value = 0.01, min=0.0)
'''
run the fitting
'''
#print x_data
result = lmfit.minimize(lorentzian_fit, params, args = (x_data, y_data))

lmfit.report_errors(params)

fit_values  = y_data + result.residual
x_fitted = np.arange(np.min(x_data),np.max(x_data),(np.max(x_data)-np.min(x_data))/100)
y_fitted = lorentzian_model(params,np.arange(np.min(x_data),np.max(x_data),(np.max(x_data)-np.min(x_data))/100))
pyplot.plot(x_fitted, y_fitted, 'r', label = 'fitted',linewidth=3.0)


# 175747 V = 0.9
# 180132 V = 1.1
# 180533 V = 1.3 
# 181110 V = 0.7
# 435 spectrum 185131

# ground_state = data1[:,1]
# excited_state = data1[:,2]
# total_state = data1[:,3]
# ex_09 = V_09[:,4][1:]
# horizon_09 = np.arange(np.size(ex_09))+15.5
# ex_11 = V_11[:,4][10:]
# horizon_11 = np.arange(np.size(ex_11))
# ex_13 = V_13[:,4][12:]
# horizon_13 = np.arange(np.size(ex_13))+7
# ex_07 = V_07[:,4][20:]
# horizon_07 = np.arange(np.size(ex_07))+25.5

#pyplot.plot(excitation1[:200],'o-')
#pyplot.plot(horizon_09,ex_09,'o-')
#pyplot.plot(horizon_11,ex_11,'o-')
#pyplot.plot(horizon_13,ex_13,'o-')
#pyplot.plot(horizon_07,ex_07,'o-')
#pyplot.plot(np.array([74,83.22,93.6,102.6]),np.array([0.7,0.9,1.1,1.3]), 'o-')
pyplot.plot(x_data,spectrum1,'o')
pyplot.show()
# freq_array = data132[:,0]
# stage_C1_gain_array = 10*np.log(data132[:,1])
# 
# #data134 = stage C gain#
# data134 = np.loadtxt(open("134.csv",'rb'),delimiter=',',skiprows=1)
# stage_C2_gain_array = 10*np.log(data134[:,1])
# 
# 
# 
# 
# ## plot all responses ##
# pyplot.plot(freq_array,stage_C1_gain_array)
# pyplot.plot(freq_array,stage_C2_gain_array)
# 
# ## change to log scale (y scale already in dB###
# pyplot.xscale('log',basey = 10,subsy=[2, 3, 4, 5, 6, 7, 8, 9])
# pyplot.xlim([50,5000000])
# 
# ## control the size of the plot
# fig = matplotlib.pyplot.gcf()
# fig.set_size_inches(6,4)

# pyplot.show()

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

# 175747 V = 0.9
# 180132 V = 1.1
# 180533 V = 1.3 
# 181110 V = 0.7
# 435 spectrum 185131

# ground_state = data1[:,1]
# excited_state = data1[:,2]
# total_state = data1[:,3]
ex_09 = V_09[:,4][1:]
horizon_09 = (np.arange(np.size(ex_09))+15.5)*2.0-157
ex_11 = V_11[:,4][10:]
horizon_11 = (np.arange(np.size(ex_11)))*2.0-157
ex_13 = V_13[:,4][12:]
horizon_13 = (np.arange(np.size(ex_13))+7)*2.0-157
ex_07 = V_07[:,4][20:]
horizon_07 = (np.arange(np.size(ex_07))+25.5)*2.0-157

#pyplot.plot(excitation1[:200],'o-')
pyplot.plot(horizon_09,ex_09,'o-')
#pyplot.plot(horizon_11,ex_11,'o-')
pyplot.plot(horizon_13,ex_13,'o-')
#pyplot.plot(horizon_07,ex_07,'o-')
#pyplot.plot(np.array([74,83.22,93.6,102.6]),np.array([0.7,0.9,1.1,1.3]), 'o-')
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

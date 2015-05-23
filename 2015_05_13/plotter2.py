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

data_list = [["data_gyro_05_18/150518145137stab.dat",400],
            ["data_gyro_05_18/150518155805stab.dat",400]]
             #"data_gyro_05_13/150513161319stab.dat"]

## zeeman 1 = data_1[:,7]
## zeeman 2 = data_1[:,8]
## lock indicator = 14,15,16,17

total_data = np.array([])

for i in range(int(np.size(data_list)/2)):
    data_1 = np.loadtxt(data_list[i][0], skiprows=data_list[i][1]) 
    data_1_lock = data_1[:,14]*data_1[:,15]*data_1[:,16]*data_1[:,17]
    ratio_1 = data_1[:,7]/data_1[:,8]
    where_lock_1 = np.where(data_1_lock>0.5)
    ratio_cut_1 = ratio_1[where_lock_1]
    ratio_cut_1 = ratio_cut_1[:np.size(ratio_cut_1)/2]
    total_data = np.append(total_data,ratio_cut_1)
    
#mea_number_1 = data_1[:,0][where_lock_1]

#pyplot.plot(data_1[:,7]/data_1[:,8])

ratio_average = np.average(total_data)
fractional_error = (np.std(total_data)/np.sqrt(np.size(total_data)))/np.average(total_data)
gamma = -(1-ratio_average)/(1+ratio_average)

print "average = ", ratio_average
print "fractional error = ", fractional_error

print gamma, "pm", gamma*fractional_error/1.69

pyplot.plot(total_data)
#pyplot.plot(mea_number_1%7)

pyplot.show()

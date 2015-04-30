from __future__ import division
import numpy as np
from matplotlib import pyplot
import matplotlib
import lmfit


def linear_model(params, x):
    A = params['A'].value
    B = params['B'].value
    output = A+B*x
    #output = A/(x**B)
    return output
'''
define how to compare data to the function
'''
def linear_fit(params , x, data):
    model = linear_model(params, x)
    return (model - data)





ratio = 2.62931420989890960

Sr_time_offset = 43887229.263617
Hg_time_offset = 3512987633.790

Hg = np.loadtxt("Hgfile/150427203617stab_cut.dat",skiprows=1)
Hg_raw_time = Hg[:,3]-Hg[:,3][-1]
#Hg_raw_time = Hg[:,3]-Hg_time_offset
Hg_freq = Hg[:,1]-Hg[:,1][-1]
#Sr_raw_freq = Sr[]

#Hg[:,7] excitation rate

t_result = Hg_raw_time
f_result = Hg[:,7]

pyplot.plot(t_result,f_result)

x = t_result
y = f_result

params = lmfit.Parameters()

params.add('A', value = 5.96)
params.add('B', value = 0.0)

result = lmfit.minimize(linear_fit, params, args = (x, y))

fit_values  = y + result.residual

lmfit.report_errors(params)

print "chi_squared is ", result.redchi

x_plot = np.linspace(np.min(x),np.max(x),1000)
pyplot.plot(x_plot,linear_model(params,x_plot),linewidth = 1.3, linestyle = '--', color = "#003300",zorder=2)

#pyplot.plot(Sr_time, Sr_freq*ratio)
#pyplot.plot(Hg_raw_time, Hg_freq)

pyplot.show()

# ## set grid
# pyplot.grid(True, which='both')
# 
# ## set plot limit
# pyplot.xlim([-0.1,1.2])
# pyplot.ylim([-1.0,22])
# 
# pyplot.show()
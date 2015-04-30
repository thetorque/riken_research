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


for i in range(100):
    Sr = np.loadtxt("data04.dat") ## Load Sr
    Hg = np.loadtxt("Hgfile/150427203617stab_cut.dat",skiprows=1)
    Sr_raw_time = Sr[:,15] - Sr[:,15][-i] ## load time column and minus the initial time offset
    #Sr_raw_time = Sr[:,15] - Sr_time_offset
    Hg_raw_time = Hg[:,3]-Hg[:,3][-1]
    #Hg_raw_time = Hg[:,3]-Hg_time_offset
    Sr_freq = Sr[:,2]-Sr[:,2][-1]
    Hg_freq = Hg[:,1]-Hg[:,1][-1]
    #Sr_raw_freq = Sr[]
    
    
    Sr_time = Sr_raw_time[-np.size(Hg_freq):]
    Sr_freq = Sr_freq[-np.size(Hg_freq):]
    
    ####
    
    f_result = np.array([])
    t_result = np.array([])
    
    for f,t in zip(Hg_freq,Hg_raw_time):
        
        Sr_f = Sr_freq[np.where((Sr_time<(t+0.3)) & (Sr_time>(t-0.3)))] ## look for Sr at the same time
        if (np.size(Sr_f)==1):
            f_diff = Sr_f*ratio-f
            t_result = np.append(t_result,t)
            f_result = np.append(f_result,f_diff)
    
    print np.sum(np.sqrt(f_result**2)), i

# ## set grid
# pyplot.grid(True, which='both')
# 
# ## set plot limit
# pyplot.xlim([-0.1,1.2])
# pyplot.ylim([-1.0,22])
# 
# pyplot.show()
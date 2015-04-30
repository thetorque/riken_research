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

ratio = 2.62931420989890960

Sr_time_offset = 43887229.263617
Hg_time_offset = 3512987633.790

Sr = np.loadtxt("data04.dat") ## Load Sr
Hg = np.loadtxt("Hgfile/150427203617stab_cut.dat",skiprows=1)
Sr_raw_time = Sr[:,15] - Sr[:,15][-5] ## load time column and minus the initial time offset
print "time offset for Sr is ", Sr[:,15][-5]
#Sr_raw_time = Sr[:,15] - Sr_time_offset
Hg_raw_time = Hg[:,3]-Hg[:,3][-1]
print "time offset for Sr is ", Hg[:,3][-1]
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
    
    Sr_f = Sr_freq[np.where((Sr_time<=(t+0.03)) & (Sr_time>=(t-0.03)))] ## look for Sr at the same time
    if (np.size(Sr_f)==1):
        f_diff = Sr_f*ratio-f
        t_result = np.append(t_result,t)
        f_result = np.append(f_result,f_diff)


t_result = t_result - t_result[0]

time = t_result



freq = f_result
#freq_uncorrected = np.load('2014_04_18_weekend_freq_no_phase_correction.npy')
#phase = freq

freq_average = np.average(freq)
freq_std = np.std(freq)

print "average frequency shift = ", freq_average, "pm", freq_std/np.sqrt(np.size(freq)-1)

phase = freq

interval = time[1:]-time[0:-1]
print "minimum interval is", np.min(interval)

#start_bin_size = max(interval)+1 # choose bin size to have at least one data point
start_bin_size = 20
smallest_bin_size = min(interval)

print "smallest bin size =", smallest_bin_size
print "Start bin size = ", start_bin_size

##### Calculate allan deviation ####
bin_array = []
true_variance = []
avar = []
allan_error_bar = []
 
for bin_size in np.logspace(np.log10(start_bin_size),np.log10(time[-1]/3.0),num=30):
    phase_diff = []
    #print "bin_size = ", bin_size
    cf = bin_size/smallest_bin_size+1
    
    #cf = bin_size/smallest_bin_size
    print "Averaging factor = ", cf
    for j in range(0,int(cf)):
        time_offset = bin_size*j/(cf)
        for i in range(0,int(np.floor(max(time-time_offset)/bin_size))-1):
            time1 = time_offset+bin_size*i
            time2 = time1+bin_size
            time3 = time2+bin_size
            where1 = np.where((time1<=time)&(time<time2))
            where2 = np.where((time2<=time)&(time<time3))
            ## skip if there is no data point in the time slice
            if not np.size(phase[where1])*np.size(phase[where2]):
                print "no data at t = ", time1
                continue
            mean_phase1 = np.average(phase[where1])
            mean_phase2 = np.average(phase[where2])
            mean_phase_diff = (mean_phase2-mean_phase1)**2/2.0 ### calculate phase difference squared
            phase_diff.append(mean_phase_diff)
 
    bin_array.append(bin_size)
    avar_result = np.sqrt(np.average(phase_diff))
    avar.append(avar_result)
    M = np.size(phase_diff)
    allan_error_bar.append(avar_result*np.sqrt(0.5/(M)))
    
x = np.array(bin_array)
y = np.array(avar)
yerr = np.array(allan_error_bar)*np.sqrt(2.087)

#print x, y, yerr

params = lmfit.Parameters()

params.add('A', value = 5.96)
params.add('B', value = 0.5, vary = False)

result = lmfit.minimize(allan_fit, params, args = (x, y, yerr))

fit_values  = y + result.residual

lmfit.report_errors(params)

print "chi_squared is ", result.redchi

plt = pyplot.figure(0)
ax = plt.add_subplot(111)
ax.set_axisbelow(True)
###
pyplot.grid(True, which='both', color='#DDE4DD', linestyle='-', linewidth=0.5,zorder=-1)
###
#plt.add_subplot(111, axisbg='#FFFAFA')
#pyplot.errorbar(x,y,yerr*np.sqrt(result.redchi),fmt='o',ecolor = '#1F3ABA',elinewidth=2.0, color='#1F3ABA', markersize = 8.0,zorder=3)
pyplot.errorbar(x,y,yerr,fmt='o',ecolor = '#1F3ABA',elinewidth=2.0, color='#1F3ABA', markersize = 8.0,zorder=3)


##############################################


x_plot = np.linspace(np.min(x),np.max(x),1000)
# pyplot.plot(x_plot,allan_model(params,x_plot),linewidth = 1.3, linestyle = '--', color = "#003300",zorder=2)
#############################################

#quantum_projection = 2.3/np.sqrt(x_plot)
# quantum_projection = 1.7/np.sqrt(x_plot)
# pyplot.plot(x_plot,quantum_projection,linewidth = 1.3,linestyle = '-',color = "#E62F3B",zorder=1)
#quantum_projection = 2.7/np.sqrt(x_plot)
#pyplot.plot(x_plot,quantum_projection,linewidth = 1.3,linestyle = '-',color = "black",zorder=1)
  
pyplot.xscale('log')
pyplot.yscale('log',basey = 10,subsy=[2, 3, 4, 5, 6, 7, 8, 9])
    
# ytick = [0.01,0.02,0.03,0.05,0.1,0.2,0.3,0.5]
# pyplot.yticks(ytick,ytick)
# xtick = [50,100,200,500,1000,2000,5000,10000, 20000, 50000]
# pyplot.xticks(xtick,xtick)
#  
#  
# pyplot.ylim([0.01,0.5])
# pyplot.xlim([50,35000])

pyplot.show()

import numpy as np
import matplotlib
from matplotlib import pyplot

## plot data of c parameters

pyplot.grid(True, which='both', color='#DDE4DD', linestyle='-', linewidth=0.5,zorder=-1)

#pyplot.plot([2017],[3.4e-20],'o',zorder=3) #HCI
pyplot.plot([2014],[7.4e-19],'o',zorder=3) #Berkeley
pyplot.plot([2013],[6e-17],'o',zorder=3) #Hohensee
pyplot.plot([2007],[6.3e-16],'o',zorder=3) #[46]
pyplot.plot([2005],[6.3e-16],'o',zorder=3) #[47]
pyplot.plot([2003],[1.6e-14],'o',zorder=3) #[48]
pyplot.plot([2006],[5e-15],'o',zorder=3) #[50]

pyplot.yscale('log',basey = 10,subsy=[2, 3, 4, 5, 6, 7, 8, 9])

xtick = [2001,2004,2007,2010,2013,2016]

pyplot.xticks(xtick,xtick)
pyplot.ylim([1e-19,1e-13])

## control the size of the plot
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(6,4)

pyplot.show()

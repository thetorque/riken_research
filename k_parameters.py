import numpy as np
from matplotlib import pyplot

## plot data of c parameters

pyplot.grid(True, which='both', color='#DDE4DD', linestyle='-', linewidth=0.5,zorder=-1)
pyplot.plot([2014],[2.2e-18],'o',zorder=3) #Berkeley
pyplot.plot([2010],[0.6e-16],'o',zorder=3) #[95]
pyplot.plot([2009],[0.73e-17],'o',zorder=3) #[96]
pyplot.plot([2009],[1.3e-17],'o',zorder=3) #[97]
#pyplot.plot([2017],[0.6e-17],'o',zorder=3) #[98]
pyplot.plot([2007],[4.0e-16],'o',zorder=3) #[46]
pyplot.plot([2006],[2.3e-16],'o',zorder=3) #[99]
pyplot.plot([2005],[2.5e-16],'o',zorder=3) #[100]
pyplot.plot([2005],[0.43e-15],'o',zorder=3) #[101]
pyplot.plot([2005],[1.6e-15],'o',zorder=3) #[47]
pyplot.plot([2004],[2.3e-15],'o',zorder=3) #[102]
pyplot.plot([2003],[2.6e-15],'o',zorder=3) #[103]
pyplot.plot([2003],[1.4e-13],'o',zorder=3) #[104]

pyplot.yscale('log',basey = 10,subsy=[2, 3, 4, 5, 6, 7, 8, 9])

xtick = [2002,2004,2006,2008,2010,2012,2014]
pyplot.xticks(xtick,xtick)

pyplot.show()

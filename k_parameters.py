import numpy as np
from matplotlib import pyplot
import matplotlib

## plot data of c parameters

pyplot.grid(True, which='both', color='#DDE4DD', linestyle='-', linewidth=0.5,zorder=-1)
#pyplot.plot([2014],[1.5e-18],'o',zorder=3,color='#FF3300') #Berkeley
pyplot.plot([2010],[0.6e-16],'o',zorder=3,color='#0404B4') #[95]
pyplot.plot([2009],[0.73e-17],'o',zorder=3,color='#0404B4') #[96]
pyplot.plot([2009],[1.3e-17],'o',zorder=3,color='#0404B4') #[97]
#pyplot.plot([2017],[0.6e-17],'o',zorder=3) #[98]
pyplot.plot([2007],[4.0e-16],'o',zorder=3,color='#0404B4') #[46]
pyplot.plot([2006],[2.3e-16],'o',zorder=3,color='#0404B4') #[99]
pyplot.plot([2005],[2.5e-16],'o',zorder=3,color='#0404B4') #[100]
pyplot.plot([2005],[0.43e-15],'o',zorder=3,color='#0404B4') #[101]
pyplot.plot([2005],[1.6e-15],'o',zorder=3,color='#0404B4') #[47]
pyplot.plot([2004],[2.3e-15],'o',zorder=3,color='#0404B4') #[102]
pyplot.plot([2003],[2.6e-15],'o',zorder=3,color='#0404B4') #[103]
pyplot.plot([2003],[1.4e-13],'o',zorder=3,color='#0404B4') #[104]

pyplot.plot([1881],[1e-8],'o',zorder=3,color='#8A4B08') #Michelson
pyplot.plot([1887],[1e-9],'o',zorder=3,color='#8A4B08') #Michelson Morley
pyplot.plot([1904],[1e-10],'o',zorder=3,color='#8A4B08') #Morley Miller
pyplot.plot([1926],[3e-12],'o',zorder=3,color='#8A4B08') #Kennedy
pyplot.plot([1927],[1e-10],'o',zorder=3,color='#8A4B08') #Illingworth
pyplot.plot([1930],[3e-11],'o',zorder=3,color='#8A4B08') #Joos
pyplot.plot([1955],[1e-13],'o',zorder=3,color='#0404B4') #Essen
pyplot.plot([1958],[1.2e-14],'o',zorder=3,color='#0404B4') #Cedarholm
pyplot.plot([1979],[3e-15],'o',zorder=3,color='#0404B4') #Brillet Hall


pyplot.yscale('log',basey = 10,subsy=[2, 3, 4, 5, 6, 7, 8, 9])

xtick = [1880,1900,1920,1940,1960,1980,2000,2020]

pyplot.xticks(xtick,xtick)
pyplot.xlim([1880,2020])
pyplot.ylim([1e-19,1e-7])

## control the size of the plot
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(8,5)

pyplot.show()

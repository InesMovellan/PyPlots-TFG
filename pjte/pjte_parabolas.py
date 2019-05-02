import numpy as np
import matplotlib.pyplot as plt
#importar todas las funciones de pylab
from pylab import *

x = arange(-10,10,0.01)  
x1 = arange(-4,4,0.005)  
x2 = arange(4,10,0.005)
x3 = arange(-10,-4,0.005)
y =0.10*x**2
y1 =0.30*x**2
y2 = 0.30*x**2+25
y3 = 0.50*x**2+25
y4 = 0.60*-x1**2
y5 = 0.60*(x2-7)**2-15.01
y6 = 0.60*(x3+7)**2-15.01
fig = plt.figure()
p = fig.add_subplot(111)
plt.axhline(y=min(y), linewidth=2, color='k')
plt.axvline(x=0, linewidth=2, color='k')
p.plot(x, y, 'b', x, y1, 'k--', x, y2, 'k--', x, y3, 'k', x1, y4, 'r', x2, y5, 'r', x3, y6, 'r', linewidth=2)
text(10.1,9,'$E_{-}$', fontsize=25, color='b')
text(10.1,-10.7,'$E_{-}$', fontsize=25, color='r')
text(10.1,73,'$E_{+}$', fontsize=25, color='k')
text(-11.8,9,'$K>0$', fontsize=25, color='b')
text(-11.8,-10.7,'$K<0$', fontsize=25, color='r')
text(9,-5,'$Q_g$', fontsize=25, color='k')
text(0.2,75,'$E$', fontsize=25, color='k')
plt.xlim(-12,12)
plt.show()
fig.savefig("PJTE.png")


#namefile = "EnergiaDistancia.txt"

#x = []
#y = []

#with open(namefile, 'r') as fr:
#    for i in range(0,13):
#        x.append(float(fr.readline()))
#    for i in range(0,13):
#        y.append(float(fr.readline()))
#x = np.asarray(x)
#x += 0.104
#y = np.asarray(y)
#y = y*27.2114
#y += 18263.30893027034
#for i in range(0,13):
	#y[i] = y[i] + 18263.30893027034

#namefile1 = "EnergiaDistancia1.txt"

#x1 = []
#y1 = []

#with open(namefile1, 'r') as fr:
#    for i in range(0,11):
#        x1.append(float(fr.readline()))
#    for i in range(0,11):
#        y1.append(float(fr.readline()))
#x1 = np.asarray(x1)
#x1 -=0.07
#y1 = np.asarray(y1)
#y1 = y1*27.2114

#fig = plt.figure()
#p = fig.add_subplot(111)
#p.plot(x, y, 'bo', x1, y1, 'bo', markersize = 6)
#p.plot(x, y, 'b', x1, y1, 'b', linewidth=2)
#plt.ylim((-18263.31,-18263.23))
#plt.axhline(y=min(y1),linewidth=1, color='k', linestyle='--')
#plt.axhline(y=min(y),linewidth=1, color='k', linestyle='--')
#plt.xlim((min(x1),max(x)))
#p.set_xlabel('$d$ / $\AA$', fontsize=27)
#p.set_ylabel('$E$ / $eV$', fontsize=27)
#for tick in p.xaxis.get_major_ticks():
#	tick.label.set_fontsize(23)
#for tick in p.yaxis.get_major_ticks():
#	tick.label.set_fontsize(23)
#plt.show()
#fig.savefig("NaF_JT.png")

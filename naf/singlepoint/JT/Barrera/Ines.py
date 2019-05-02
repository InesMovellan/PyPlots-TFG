import numpy as np
import matplotlib.pyplot as plt
from pylab import *

namefile = "ed.txt"

x = []
y = []

with open(namefile, 'r') as fr:
    for i in range(0,9):
        x.append(float(fr.readline()))
    for i in range(0,9):
        y.append(float(fr.readline()))
x = np.asarray(x)
x += 0.104
y = np.asarray(y)
y = y*27.2114
x -=0.004
#y += 18263.30893027034
#for i in range(0,13):
	#y[i] = y[i] + 18263.30893027034

namefile1 = "ed1.txt"

x1 = []
y1 = []

with open(namefile1, 'r') as fr:
    for i in range(0,8):
        x1.append(float(fr.readline()))
    for i in range(0,8):
        y1.append(float(fr.readline()))
x1 = np.asarray(x1)
x1 -=0.074
y1 = np.asarray(y1)
y1 = y1*27.2114

fig = plt.figure()
p = fig.add_subplot(111)
p.plot(x, y, 'bo', x1, y1, 'bo', markersize = 6)
p.plot(x, y, 'b', x1, y1, 'b', linewidth=2)
plt.xlim((-0.2,0.2))
#plt.ylim((-18263.31,-18263.23))
plt.axhline(y=min(y1),linewidth=1, color='k', linestyle='--')
plt.axhline(y=min(y),linewidth=1, color='k', linestyle='--')
plt.xlim((min(x1),max(x)))
plt.annotate(s='', xy=(0.0,max(y)-0.34), xytext=(0.0,min(y)-0.005),
					 arrowprops=dict(arrowstyle='<->'))
plt.annotate(s='', xy=(0.153,max(y)-0.502), xytext=(0.153,min(y)+0.022),
					 arrowprops=dict(arrowstyle='<-'))
plt.annotate(s='', xy=(0.153,max(y)-0.560), xytext=(0.153,min(y)-0.030),
					 arrowprops=dict(arrowstyle='->'))


'''
plt.annotate(s='', xy=(0.24,min(y)+0.01), xytext=(0.24,min(y)-0.04),
					 arrowprops=dict(arrowstyle='->'))
plt.annotate(s='', xy=(0.24,min(y)+0.08), xytext=(0.24,min(y)+0.02),
					 arrowprops=dict(arrowstyle='<-'))
'''
text(0.003,max(y)-0.47, '$E_{JT}$', fontsize=22, color='k')
text(0.156,max(y)-0.53, '$B$', fontsize=22, color='k')

p.set_xlabel('$d$ / $\AA$', fontsize=27)
p.set_ylabel('$E$ / $eV$', fontsize=27)
for tick in p.xaxis.get_major_ticks():
	tick.label.set_fontsize(23)
for tick in p.yaxis.get_major_ticks():
	tick.label.set_fontsize(23)
plt.show()
fig.savefig("NaF_JT.png")

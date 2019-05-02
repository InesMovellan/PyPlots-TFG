import numpy as np
import matplotlib.pyplot as plt

namefile = "EnergiaDistancia.txt"

x = []
y = []

with open(namefile, 'r') as fr:
    for i in range(0,13):
        x.append(float(fr.readline()))
    for i in range(0,13):
        y.append(float(fr.readline()))
#x = np.asarray(x)
#x += 0.100
y = np.asarray(y)
y += 18263.30759841739
y = y*27.2114 


#for i in range(0,13):
	#y[i] = y[i] + 18263.30893027034

param = np.polyfit(x, y, 3)
#param[3] = 0

print "X0 = "+str(param[3])
print "X1 = "+str(param[2])
print "X2 = "+str(param[1])
print "X3 = "+str(param[0])

xTh = np.linspace(min(x),max(x))
yTh = param[3] + param[2]*xTh + param[1]*xTh**2 + param[0]*xTh**3 

fig = plt.figure()
p = fig.add_subplot(111)
p.plot(xTh, yTh, 'b', linewidth=2.5)
p.plot(x, y, 'bo', markersize = 8)
plt.ylim((min(y)-0.05,max(y)))
plt.xlim((min(x),max(x)))
p.set_xlabel('$d$ / $\AA$', fontsize=27)
p.set_ylabel('$E$ / $eV$', fontsize=27)
for tick in p.xaxis.get_major_ticks():
	tick.label.set_fontsize(23)
for tick in p.yaxis.get_major_ticks():
	tick.label.set_fontsize(23)
plt.show()
fig.savefig("elongatedJT.png")

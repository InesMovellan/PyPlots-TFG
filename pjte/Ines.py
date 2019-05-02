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
x = np.asarray(x)
x += 0.104
y = np.asarray(y)
y = y*27.2114
#y += 18263.30893027034
#for i in range(0,13):
	#y[i] = y[i] + 18263.30893027034

namefile1 = "EnergiaDistancia1.txt"

x1 = []
y1 = []

with open(namefile1, 'r') as fr:
    for i in range(0,11):
        x1.append(float(fr.readline()))
    for i in range(0,11):
        y1.append(float(fr.readline()))
x1 = np.asarray(x1)
x1 -=0.07
y1 = np.asarray(y1)
y1 = y1*27.2114

fig = plt.figure()
p = fig.add_subplot(111)
p.plot(x, y, 'bo', x1, y1, 'bo', markersize = 6)
p.plot(x, y, 'b', x1, y1, 'b', linewidth=2)
#plt.ylim((-18263.31,-18263.23))
plt.axhline(y=min(y1),linewidth=1, color='k', linestyle='--')
plt.axhline(y=min(y),linewidth=1, color='k', linestyle='--')
plt.xlim((min(x1),max(x)))
p.set_xlabel('$d$ / $\AA$', fontsize=27)
p.set_ylabel('$E$ / $eV$', fontsize=27)
for tick in p.xaxis.get_major_ticks():
	tick.label.set_fontsize(23)
for tick in p.yaxis.get_major_ticks():
	tick.label.set_fontsize(23)
plt.show()
fig.savefig("NaF_JT.png")

# -*- coding: utf-8 -*-

from matplotlib import rcParams
import numpy as np
import matplotlib.pyplot as plt
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['DejaVu Sans', 'Tahoma']

namefile = "pressureDistance.txt"

x = []
y = []
y1 = []
y2 = []
with open(namefile, 'r') as fr:
   for i in range(0,5):
      x.append(float(fr.readline()))
   for i in range(0,5):
      y.append(float(fr.readline()))
   for i in range(0,5):
      y1.append(float(fr.readline()))
   for i in range(0,5):
      y2.append(float(fr.readline()))

#param = np.polyfit(x, y, 1)

#xTh = np.linspace(min(x), max(x))
#yTh = param[1] + param[0]*xTh

fig = plt.figure()
ax = fig.add_subplot(111)
#plt.plot(xTh, yTh, 'r')
ax.plot(x, y, 'ro')
ax.plot(x, y, 'r', label = "$R_{ax}$")
ax.plot(x, y1, 'bo')
ax.plot(x, y1, 'b', label = "$R_{eq}$")
ax.plot(x, y2, 'go')
ax.plot(x, y2, 'g', label="$R_{eq}$")
ax.set_xlabel('$P$ / $GPa$', fontsize=22)
ax.set_ylabel('$R$ / $\AA$', fontsize=22)
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(20)
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(20)
ax.legend()
plt.show()
fig.savefig("pressure.png")

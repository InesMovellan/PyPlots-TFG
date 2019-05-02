import numpy as np
import matplotlib.pyplot as plt

namefile = "EnergiaDistancia.txt"

x = []
y = []
x1 = []
y1 = []
with open(namefile, 'r') as fr:
   for i in range(0,6):
      x.append(float(fr.readline()))
   for i in range(0,6):
      y.append(float(fr.readline()))
   for i in range(0,6):
      x1.append(float(fr.readline()))
   for i in range(0,6):
      y1.append(float(fr.readline()))
param = np.polyfit(x, y, 3)
param1 = np.polyfit(x1, y1, 3)

print "X0r = "+str(param[3])
print "X1r = "+str(param[2])
print "X2r = "+str(param[1])
print "X3r = "+str(param[0])

print "X0b = "+str(param1[3])
print "X1b = "+str(param1[2])
print "X2b = "+str(param1[1])
print "X3b = "+str(param1[0])



xTh = np.linspace(min(x), max(x))
yTh = param[3] + param[2]*xTh + param[1]*xTh**2 + param[0]*xTh**3
xTh1 = np.linspace(min(x1), max(x1))
yTh1 = param1[3] + param1[2]*xTh1 + param1[1]*xTh1**2 + param1[0]*xTh1**3

fig = plt.figure()
plt.plot(xTh, yTh, 'r')
plt.plot(xTh1, yTh1, 'b')
plt.plot(x, y, 'ro')
plt.plot(x1, y1, 'bo')
plt.xlabel('$d$ / $\AA$')
plt.ylabel('$E$ / $UA$')
plt.show()
fig.savefig("singlepoint.png")

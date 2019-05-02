import numpy as np
import matplotlib.pyplot as plt
# Holi
namefile = "EnergiaDistancia.txt"

x = [0,1,2,3,4,5]
y = [0,1,2,3,4,5]
with open(namefile, 'r') as fr:
	for i in range(0,6):
		line = fr.readline()
		values = line.split("\t")
		x[i] = float(values[0])
		y[i] = float(values[1])
print x
print y
plt.plot(x, y, 'o')
plt.show() 

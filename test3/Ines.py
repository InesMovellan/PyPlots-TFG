import numpy as np
import matplotlib.pyplot as plt

namefile = "EnergiaDistancia.txt"

x = []
y = []

with open(namefile, 'r') as fr:
	line = fr.readline()
	while line != '':
		values = line.split("\t")
		x.append(float(values[0]))
		y.append(float(values[1]))
		line = fr.readline()

w = open ("output.txt", "w")
for i in range (0,len(x)):
	w.write(str(x[i]) + '\t'+str(y[i]) + '\n')

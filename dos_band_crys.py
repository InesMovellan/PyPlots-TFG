##############################################################################
#############################     BANDS AND DOS     ##########################
##############################################################################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc                         
from matplotlib.ticker import FormatStrFormatter  
from scipy.interpolate import interp1d            
import sys

font = {'family' : 'serif',   
        'weight' : 'normal',  
        'size' : '15'         
       }                      
plt.rc('font', **font)        

# Create the variables 
E = []
dos = []
k = []

# Read the information from the calculations 
f = open('run_dat.DOSS','r')
line = f.readline()
while line:
    l = line.split()
    E.append(float(l[0]))
    dos.append(float(l[1])) 
    line = f.readline() 
f.close()

# Energy in eV
E = np.asarray(E)
E = E*27.2114 

# Plot bands
fig = plt.figure()
p = fig.add_subplot(121)

f = open('bands_out','r')
line = f.readline()
while line:
    l = line.split()
    k.append(float(l[0]))
    line = f.readline()
f.close()

for j in range(1,26):
    f = open('bands_out','r')
    band = []
    for i in range(0,len(k)):
        line = f.readline()
        l = line.split()
        band.append(float(l[j]))
    f.close()
    band = np.asarray(band)
    band = band*27.2114
    p.plot(k,band,'g')

plt.hlines(0.0, min(k), max(k), colors='r', linestyles='solid')
p.set_ylabel('E-E$_{F}$ (eV)') 
p.set_xlabel('k')   
axes = plt.gca()
axes.set_ylim([-6,max(E)])
axes.set_xlim([min(k),max(k)])

# Plot DOS. It should be change in the case of close shell system
p = fig.add_subplot(122)
p.plot(dos,E,'g') 
p.set_ylabel('E-E$_{F}$ (eV)') 
p.set_xlabel('DOS')   
axes = plt.gca()
plt.hlines(0.0, 0, 500, colors='r', linestyles='solid')
axes.set_ylim([-6,max(E)])
axes.set_xlim([0,400])
plt.show()
fig.savefig('crystal_bands_dos_srtio3_pure.png')

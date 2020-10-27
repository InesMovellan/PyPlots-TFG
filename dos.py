##############################################################################
#############################   DENSITY OF STATES   ##########################
##############################################################################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc                         
from matplotlib.ticker import FormatStrFormatter  
from scipy.interpolate import interp1d            

font = {'family' : 'serif',   
        'weight' : 'normal',  
        'size' : '15'         
       }                      
plt.rc('font', **font)        

# Create the variables 
E = []
up = []
down = []

# Read the information from the calculations 
f = open('up','r')
line = f.readline()
while line:
    l = line.split()
    E.append(float(l[0]))
    up.append(float(l[1])) 
    line = f.readline() 
f.close()

f = open('down','r')
line = f.readline()
while line:
    l = line.split()
    down.append(float(l[1]))
    line = f.readline()
f.close()

# Check whether the spin up and spin down cancel or not (they should cancel in an
# AFM system)
up = np.asarray(up)
down = np.asarray(down)
dif = up + down

# Plot DOS and dif. It should be change in the case of close shell system
fig = plt.figure()
p = fig.add_subplot(111)
p.plot(E,up,'r', linewidth=1.0, label='spin up') 
p.plot(E,down,'b', linewidth=1.0, label='spin down') 
p.plot(E, dif, 'm', linewidth=1.0)
p.set_xlabel('E-E$_{F}$ (Ha)') 
p.set_ylabel('DOS')   
plt.title('DOS K$_2$CuF$_4$ AFM', fontsize=16)
plt.legend()
axes = plt.gca()
plt.vlines(0.0, min(down), max(up), colors='k', linestyles='dashed', label='E$_F$')
axes.set_xlim([min(E),max(E)])
plt.show()
fig.savefig('dos-k2cuf4.png')

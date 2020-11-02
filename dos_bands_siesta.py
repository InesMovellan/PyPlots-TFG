# This script plots the bands of a system obtained with gnubands using XX.bands (from siesta) as
# input

# The script does not plot every band, only the ones 10 eV above and below Fermi energy

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

font = {'family' : 'serif',
        'weight' : 'normal',
        'size' : '15'
       }
plt.rc('font', **font)

# The file which contains the value of k and E is opened
fr = open('bandsGGA.txt','r')

# The script reads the title and store some variables
for i in range (0,16):
    line=fr.readline()
    if i==6:
       # Fermi energy is stored in the variable Ef (we will shift the bands plot)
       l = line.split()
       Ef = float(l[3])
    if i==9:
       # Number of bands nb and number of k points are defined
       l = line.split()
       nb = int(l[5])
       nk = int(l[7])



# Figure is opened
fig = plt.figure()
p = fig.add_subplot(121)

# Read the blocks of k points and energies (72 bands, 72 blocks and 150 points for each band)
for j in range(0,nb):
    # The lists k and E that will store the values are defined
    k = []
    E = []
    for i in range (0,nk):
        line = fr.readline()
        l = line.split()
        k.append(float(l[0]))
        E.append(float(l[1]))
        # The origin (zero) is shifted to Fermi energy
        E[i] = E[i] - Ef
    fr.readline()
    fr.readline()
    # The bands are plotted
    p.plot(k,E, c='b')
fr.close()

# Plot details
plt.hlines(0.0, min(k), max(k), colors='r', linestyles='solid')
plt.vlines(0.43, -6, 9, colors='k', linestyles='dashed')
plt.vlines(0.86, -6, 9, colors='k', linestyles='dashed')
plt.vlines(1.465, -6, 9, colors='k', linestyles='dashed')
plt.vlines(2.21, -6, 9, colors='k', linestyles='dashed')
plt.text(-0.01, -6.8, '$\Gamma$') #, fontdict=None, withdash=<deprecated parameter>, **kwargs
plt.text(0.38, -6.8, 'X')
plt.text(0.81, -6.8, 'M')
plt.text(1.415, -6.8, '$\Gamma$')
plt.text(2.16, -6.8, 'R')
plt.text(2.75, -6.8, 'X')
frame = plt.gca()
p.set_xlabel('k',fontsize=15)
p.set_ylabel('E (eV)',fontsize=15)
frame.axes.get_xaxis().set_visible(False)
for tick in p.xaxis.get_major_ticks():
        tick.label.set_fontsize(15)
for tick in p.yaxis.get_major_ticks():
        tick.label.set_fontsize(15)
p.set_ylim([-6,8])
p.set_xlim([min(k),max(k)])
Ed = []
dos = []
#Ef = -5.8218

# The file which contains the value of k and E is opened
fr = open('SrTiO3.DOS','r')
for line in fr.readlines():
    l = line.split()
    Ed.append(float(l[0]))
    dos.append(float(l[1]))

for i in range(0,len(Ed)):
    # The origin (zero) is shifted to Fermi energy
    Ed[i] = Ed[i] - Ef
p = fig.add_subplot(122)
p.plot(dos,Ed,'b')
plt.hlines(0.0, min(dos), max(dos), colors='r', linestyles='solid')
# Plot details
p.set_xlabel('DOS (eV$^{-1}$)',fontsize=15)
p.set_ylabel('E (eV)',fontsize=15)
for tick in p.xaxis.get_major_ticks():
        tick.label.set_fontsize(15)
for tick in p.yaxis.get_major_ticks():
        tick.label.set_fontsize(15)
p.set_ylim([-6,8])
p.set_xlim([0,5])
plt.show()
fig.savefig('dos_bands_srtio3.png')

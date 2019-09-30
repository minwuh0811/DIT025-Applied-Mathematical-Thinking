# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 08:29:59 2019

@author: bishe
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib
import numpy
import matplotlib.ticker as mtick
#from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show

time=0;      # in years
deltaT= 0.3  # arbitrary, should just be sufficiently small for accuracy

krill=700000  # initial krill value
whale=2000    # initial whale value

# a,b,m,n are parameters in the model
a=0.2
b=0.0001
m=0.5
n=0.000001

timeList = []
krillList = []
whaleList = []

iniKrill=[i for i in range (300000,800000,10000)]
iniWhale=[i for i in range (1000,6000,100)]
krill, whale = numpy.meshgrid(iniKrill, iniWhale)
#Z1 = krill +  (a-b*whale)*krill    * deltaT
#Z2 = whale +  (-m+n*krill)*whale   * deltaT
Z1=(a-b*whale)*krill
Z2=(-m+n*krill)*whale
fig = plt.figure(1)
ax = fig.add_subplot(111, projection = '3d')
surf = ax.plot_surface(krill,whale,Z1 , rstride = 5, cstride = 5, cmap = matplotlib.cm.jet)
plt.title('krill(iniKrill, iniWhale)')
ax.set_zticks([])
ax.view_init(elev=90, azim=180)
fig.colorbar(surf)
plt.savefig('krill.png')
plt.show()

fig = plt.figure(2)
ax = fig.add_subplot(111, projection = '3d')
surf = ax.plot_surface(krill,whale,Z2 , rstride = 5, cstride = 5, cmap = matplotlib.cm.jet)
plt.title('whale(iniKrill, iniWhale)')
ax.set_zticks([])
ax.view_init(elev=90, azim=180)
fig.colorbar(surf)
plt.savefig('whale.png')
plt.show()

#for i in range(1200):
#
#
#	# HERE ARE THE INTERESTING FEW LINES WHERE THE FUNCTIONS ARE CREATED FROM LEFT TO RIGHT
#	# MAKE SURE YOU UNDERSTAND WHAT HAPPENS HERE!
#	
#	# time, krill and whale are updated from current values to next values
#	# the derivative(=rate of change) for each quantity determines what happens!
#
#	time = time + deltaT  # time always increased with deltaT
#	
#	krill = krill +  (a-b*whale)*krill    * deltaT
#	whale = whale +  (-m+n*krill)*whale   * deltaT
#	
#	
#	# THIS IS JUST TO PUT THE MOST RECENT VALUES IN THE LISTS
#	
#	timeList.append(time)
#	krillList.append(krill)
#	whaleList.append(whale)
#
#plt.figure(1)
#plt.subplot(211)
#plt.title('krill(t)')
#plt.plot(timeList,krillList)
#x1,x2,y1,y2 = plt.axis()
#plt.axis([0,100,300000,800000])
#
#
#plt.subplot(212)
#plt.title('whale(t)')
#plt.plot(timeList,whaleList)
#x1,x2,y1,y2 = plt.axis()
#plt.axis([0,100,0,5000])
#
#
#
#plt.tight_layout()
#plt.show()
#
#
#plt.figure(2)
#plt.title('whales and krill')
#plt.plot(whaleList,krillList)
#plt.show()

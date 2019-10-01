# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:41:31 2019

@author: bishe
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d



     # in years
deltaT= 0.3  # arbitrary, should just be sufficiently small for accuracy

   

# a,b,m,n are parameters in the model
a=0.2
b=0.0001
m=0.5
n=0.000001


List=[]

rlist=[i*0.001 for i in range(0,200) ]

for r in rlist:
    krill=700000  # initial krill value
    whale=3000 # initial whale value
    rList = []
    krillList = []
    whaleList = []
    time=0 # initial time value
    t=[]
    for i in range(200):


	# HERE ARE THE INTERESTING FEW LINES WHERE THE FUNCTIONS ARE CREATED FROM LEFT TO RIGHT
	# MAKE SURE YOU UNDERSTAND WHAT HAPPENS HERE!
	
	# time, krill and whale are updated from current values to next values
	# the derivative(=rate of change) for each quantity determines what happens!

  # time always increased with delta
          time = time + deltaT
          krill = krill+deltaT*((a-b*whale)*krill-r*whale)
          whale = whale+deltaT*(-m+n*krill)*whale    	
          krillList.append(krill)
          whaleList.append(whale)
          rList.append(r)
          t.append(time)
    List.append([krillList,whaleList,rList,t])


fig = plt.figure(1)
ax = fig.gca(projection='3d') 
print (len(List))
for i in range(len(List)): 
    ax.plot(List[i][3], List[i][2], List[i][0])   
ax.view_init(elev=0, azim=90)
ax.set_yticks([])
plt.savefig('krill_fishingEffect.png')

fig = plt.figure(2)
ax = fig.gca(projection='3d') 
print (len(List))
for i in range(len(List)): 
    ax.plot(List[i][3], List[i][2], List[i][1])   
ax.view_init(elev=0, azim=90)
ax.set_yticks([])
plt.savefig('whale_fishingeffect.png')
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:23:11 2019

@author: bishe
"""

import matplotlib.pyplot as plt


time=0;      # in minutes
deltaT= 1    # do not change!
rate=[1+2*i for i in range (60)]

temp= 5            # actual room temperature
desiredTemp=17     # desired room temperature
outsideTemp= -5     # temperature outside of room
      # for heater fan

timeList = []
tempList = []
timeMin=[]
desiredTempList = []
powerUse=[]
RateWorks=[]
timeList.append(time)
tempList.append(temp)
desiredTempList.append(desiredTemp)
powerUse.append(1000)

accError=0
for r in rate:
    time=0; 
    temp= 5;
    timeList = []
    tempList = []
    timeSet=[]
    desiredTempList = []
    maxPower=1000  
    for i in range(60):

	# you can change the controller and the maxPower of the heater
	# heater allows change once a minute to any value within 0 <= power <= maxPower
	
	# simple thermostat control - try to replace with something better!
        if temp < desiredTemp:
            maxPower = maxPower+r*deltaT
            power = maxPower
        else:
            timeSet.append(time)
            power = 0
    
		
	# simulate the physical system according to the laws of physics
	# you cannot change below!
	
	# enforce heater constraint
	
        time = time + deltaT  # time always increased with deltaT
    
	# effect of outside temperature and heater
        tempChange = 0.11 * (outsideTemp-temp) + 0.0009 * power  

        temp = temp +  tempChange * deltaT
	
	
	# THIS IS JUST TO PUT THE MOST RECENT VALUES IN THE LISTS
	
        timeList.append(time)
        tempList.append(temp)
        desiredTempList.append(desiredTemp)
        powerUse.append(power)
    if (timeSet!=[]):
            print(r)
            RateWorks.append(r)
            timeMin.append(min(timeSet))
            

plt.figure(1)
plt.title ("Rate Change Power vs time needed to reach required T")
plt.plot(timeMin,RateWorks)
plt.show()
print (timeMin)
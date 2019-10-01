# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 13:03:18 2019

@author: bishe
"""

import matplotlib.pyplot as plt


time=0;      # in minutes
deltaT= 1    # do not change!
rate=35

temp= 5            # actual room temperature
desiredTemp=17     # desired room temperature
outsideTemp= -5     # temperature outside of room
maxPower=1000        # for heater fan

timeList = []
tempList = []
desiredTempList = []
powerUse=[]
timeList.append(time)
tempList.append(temp)
desiredTempList.append(desiredTemp)
powerUse.append(1000)

accError=0
for i in range(60):

	# you can change the controller and the maxPower of the heater
	# heater allows change once a minute to any value within 0 <= power <= maxPower
	
	# simple thermostat control - try to replace with something better!
    if temp < desiredTemp:
        maxPower = maxPower+rate*deltaT
        power = maxPower
    else:
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

plt.figure(1)
plt.title('temperature(t)')
plt.plot(timeList,tempList,timeList,desiredTempList)

plt.figure(2)
plt.title('power(t)')
plt.plot(timeList,powerUse)
plt.show()
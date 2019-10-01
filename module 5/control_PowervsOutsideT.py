import matplotlib.pyplot as plt


      # in minutes
deltaT= 1    # do not change!

temp= 5            # actual room temperature
desiredTemp=17     # desired room temperature
outsideTemp= -5     # temperature outside of room
                    # for heater fan




PowerSet=[0+i*60 for i in range(60)]
outsideTemps=[-5+i*0.4 for i in range(60)]



outSideMin=[]
maxPowerMins=[]
accError=0
for outsideTemp in outsideTemps:
    timeSet=[]
    tempReach=[]
    List=[]
    for maxPower in PowerSet:
        time=0;
        temp= 5;
        timeList = []
        tempList = []
        desiredTempList = []
        for i in range(60):

	# you can change the controller and the maxPower of the heater
	# heater allows change once a minute to any value within 0 <= power <= maxPower
	
	# simple thermostat control - try to replace with something better!
            if temp < desiredTemp:
                power = maxPower
            else:
                timeSet.append(time)
                tempReach.append(maxPower)
                power = 0
            
            
            time = time + deltaT  # time always increased with deltaT
	
	# effect of outside temperature and heater
            tempChange = 0.11 * (outsideTemp-temp) + 0.0009 * power  

            temp = temp +  tempChange * deltaT
	
	
	# THIS IS JUST TO PUT THE MOST RECENT VALUES IN THE LISTS
	
            timeList.append(time)
            tempList.append(temp)
            desiredTempList.append(desiredTemp)
        List.append([timeList,tempList,desiredTempList]) 
        if (timeSet!=[]):
            outSideMin.append(outsideTemp)
            maxPowerMin=min(tempReach)
            maxPowerMins.append(maxPowerMin)

plt.figure(1)
plt.title ("Minimum power needed vs Outside temperature")
plt.plot(outSideMin,maxPowerMins)
plt.show()



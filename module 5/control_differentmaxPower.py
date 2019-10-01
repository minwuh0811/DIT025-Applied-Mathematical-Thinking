import matplotlib.pyplot as plt


      # in minutes
deltaT= 1    # do not change!

temp= 5            # actual room temperature
desiredTemp=17     # desired room temperature
outsideTemp= -5     # temperature outside of room
                    # for heater fan




PowerSet=[1000+i*40 for i in range(60)]
timeSet=[]
tempReach=[]
List=[]



accError=0
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
plt.figure(1)

plt.title('temperature(t)')
for i in range(len(List)):
    plt.plot(List[i][0],List[i][1],List[i][0],List[i][2])

plt.figure(2)

plt.title ("Maxpower vs time needed to reach required T")
plt.plot(timeSet,tempReach)
plt.show()



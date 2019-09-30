import matplotlib.pyplot as plt


time=0;      # in years
deltaT= 0.3  # arbitrary, should just be sufficiently small for accuracy

krill=700000  # initial krill value
whale=3000    # initial whale value

# a,b,m,n are parameters in the model
a=0.2
b=0.0001
m=0.5
n=0.000001

timeList = []
krillList = []
whaleList = []



for i in range(300):


	# HERE ARE THE INTERESTING FEW LINES WHERE THE FUNCTIONS ARE CREATED FROM LEFT TO RIGHT
	# MAKE SURE YOU UNDERSTAND WHAT HAPPENS HERE!
	
	# time, krill and whale are updated from current values to next values
	# the derivative(=rate of change) for each quantity determines what happens!

	time = time + deltaT  # time always increased with deltaT
	
	krill = krill +  (a-b*whale)*krill    * deltaT
	whale = whale +  (-m+n*krill)*whale   * deltaT
	
	
	# THIS IS JUST TO PUT THE MOST RECENT VALUES IN THE LISTS
	
	timeList.append(time)
	krillList.append(krill)
	whaleList.append(whale)

plt.figure(1)
plt.subplot(211)
plt.title('krill(t)')
plt.plot(timeList,krillList)

plt.subplot(212)
plt.title('whale(t)')
plt.plot(timeList,whaleList)

plt.tight_layout()
#plt.show()


#plt.figure(2)
#plt.title('whales and krill')
#plt.plot(whaleList,krillList)
plt.show()


import matplotlib.pyplot as plt


x=0.01
deltaX= 0.01

yProp=0  # THE PROPORTIONAL FUNCTION MUST BEGIN AT 0
yLinear=5
yQuad=0
yExpPlus=1
yExpMinus=1
yLog= -10
ySin=0
yCos=1

xList = []
yPropList = []
yLinearList = []
yQuadList = []
yExpPlusList = []
yExpMinusList = []
yLogList = []
ySinList = []
yCosList = []


for i in range(1250):

	# THESE ARE THE INTERESTING FEW LINES WHERE THE FUNCTIONS ARE CREATED FROM LEFT TO RIGHT
	# MAKE SURE YOU UNDERSTAND WHAT HAPPENS HERE!

	x = x + deltaX  # x IS INCREASED ONE STEP
	
	yProp = yProp + 1.3 * deltaX
	yLinear = yLinear - 0.4 * deltaX
	
	yQuad= yQuad + 1.6 * x * deltaX
	
	yExpPlus = yExpPlus + yExpPlus * deltaX
	yExpMinus = yExpMinus + (-1) * yExpMinus * deltaX
	
	yLog= yLog + 1/x * deltaX
	
	ySin = ySin + yCos * deltaX
	yCos = yCos + (-ySin) * deltaX
	
	# THIS IS JUST TO PUT THE MOST RECENT VALUES IN THE LISTS
	
	xList.append(x)
	yPropList.append(yProp)
	yLinearList.append(yLinear)
	yQuadList.append(yQuad)
	yExpPlusList.append(yExpPlus)
	yExpMinusList.append(yExpMinus)
	yLogList.append(yLog)
	ySinList.append(ySin)
	yCosList.append(yCos)


plt.subplot(331)
plt.title('proportional')
plt.plot(xList,yPropList)

plt.subplot(332)
plt.title('linear')
plt.plot(xList,yLinearList)

plt.subplot(333)
plt.title('quadratic')
plt.plot(xList,yQuadList)

plt.subplot(334)
plt.title('exponential')
plt.plot(xList,yExpPlusList)

plt.subplot(335)
plt.title('neg exponential')
plt.plot(xList,yExpMinusList)

#plt.subplot(336)
#plt.title('logarithm')
#plt.plot(xList,yLogList)

plt.subplot(337)
plt.title('sin')
plt.plot(xList,ySinList)

plt.subplot(338)
plt.title('cos')
plt.plot(xList,yCosList)

plt.subplot(339)
plt.title('sin and cos')
plt.plot(yCosList,ySinList)


plt.tight_layout()
plt.show()




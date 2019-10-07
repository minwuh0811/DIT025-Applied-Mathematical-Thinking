import matplotlib.pyplot as plt
#import random

maxRandom=4294967296
def randomLcg(seed):
    seed = (1664525 * seed + 1013904223) % maxRandom
    return seed


k=3
n=50000
sumList =[0]*(k*6+1)

seed=12345
for i in range(n):
	sum=0
	for j in range(k):
		seed = randomLcg(seed)
		die = int ( seed/maxRandom * 6 + 1 )
		#print(die)
		sum += die
	sumList[sum] += 1
	#mean=sum/k
	
meanList = [x/k for x in range(k*6+1)]

#print(mean)
	
#plt.figure(1)
#plt.title('dice plot')
#plt.plot(sumList,'ro')
#plt.show()


plt.figure(1)
plt.subplot(211)
plt.xlim(0,20)
plt.title('sum  (k='+str(k)+')')

plt.plot(sumList,'ro')

plt.subplot(212)


plt.plot(meanList,sumList,'ro')
plt.title('mean')
plt.tight_layout()
plt.show()





# alternative way to generate random number with built-in function
# die=random.randint(1,6)


# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 08:07:14 2019

@author:minwu
"""

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
    for i in range(1):
        for j in range(k):
            seed = randomLcg(seed)
            die = int ( seed/maxRandom * 6 + 1 )
		#print(die)
            sum += die   
    sumList[sum] += 1
	#mean=sum/k
print(sumList)
	
meanList = [x/k for x in range(k*6+1)]
print(meanList)
#print(mean)
	
#plt.figure(1)
#plt.title('dice plot')
#plt.plot(sumList,'ro')
#plt.show()


plt.figure(1)
plt.subplot(211)
plt.xlim(0,200)
plt.title('sum  (k='+str(k)+')')

plt.plot(sumList,'ro')

plt.subplot(212)


plt.plot(meanList,sumList,'ro')
plt.title('mean')
plt.tight_layout()
plt.show()
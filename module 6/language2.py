lang1file = open('lang1.txt','r')
lang1=lang1file.read()
lang2file = open('lang2.txt','r')
lang2=lang2file.read()

# a little preprocessing
lang1 = lang1.lower()
lang2 = lang2.lower()
n1= len(lang1)
n2= len(lang2)

# count frequencies

freq1 = [0] * 256
freq2 = [0] * 256
p1 = [0.] * 256
p2 = [0.] * 256
for c in lang1:
	if ord(c)<= 255: freq1[ord(c)] += 1
for c in lang2: 
	if ord(c)<= 255: freq2[ord(c)] += 1
	
# count bigram frequencies

freq1Bi = [([0]*256) for _ in range(256)]
freq2Bi = [([0]*256) for _ in range(256)]
p1Bi = [([0.]*256) for _ in range(256)]
p2Bi = [([0.]*256) for _ in range(256)]

#freq1Bi = [[0] * 256] * 256
#freq2Bi = [[0] * 256] * 256
#p1Bi = [[0.] * 256] * 256
#p2Bi = [[0.] * 256] * 256

prevChar=ord(' ')
for c in lang1:
	char=ord(c)
	if char >= 255: char=255
	freq1Bi[prevChar][char] += 1
	#print(chr(prevChar),prevChar,chr(char),char,freq1Bi[prevChar][char])
	prevChar=char
	
prevChar=ord(' ')
for c in lang2:
	char=ord(c)
	if char >= 255: char=255
	freq2Bi[prevChar][char] += 1
	prevChar=char
	
	


	
# create a probability model
# simplest possible assuming independence between letters
# some handling of zero frequencies - don't bother too much with this unless you want to!

s1=s2=0
for f in freq1: 
	if f>0: s1+=1
for f in freq2: 
	if f>0: s2+=1
for i,f in enumerate(freq1): p1[i]=(f+1)/(n1+s1+1)
for i,f in enumerate(freq2): p2[i]=(f+1)/(n2+s2+1)

# similar for the bigrams
s1=s2=0
for i in range(256):
	for j in range(256):
		if freq1Bi[i][j]>0: s1+=1
for i in range(256):
	for j in range(256):
		p1Bi[i][j]=(freq1Bi[i][j]+1)/(n1+s1+1)
for i in range(256):
	for j in range(256):
		if freq2Bi[i][j]>0: s2+=1
for i in range(256):
	for j in range(256):
		p2Bi[i][j]=(freq2Bi[i][j]+1)/(n2+s2+1)
	


# now calculate the probability of the string for the different languages

print("")
print("You are encouraged to play around with different strings, long and short!")

while 1:
	print("")
	string = input('Please enter a string!  ')
	string = string.lower()

	# first calculate assuming independence

	prob1=prob2=1
	for c in string: prob1 *= p1[ord(c)]
	for c in string: prob2 *= p2[ord(c)]

	# then with Markov chain

	prevChar=ord(' ')   # assume this first
	prob1Bi=1 # we have decided to have a blank first
	for c in string:
		char=ord(c)
		if char >= 255: char=255
		prob1Bi *= p1Bi[prevChar][char]/p1[prevChar]
		#print(p1Bi[prevChar][char]/p1[prevChar],"  ",p1Bi[prevChar][char] )
		prevChar=char
	#print(" " )

	prevChar=ord(' ')
	prob2Bi=1
	for c in string:
		char=ord(c)
		if char >= 255: char=255
		prob2Bi *= p2Bi[prevChar][char]/p2[prevChar]
		#print(p2Bi[prevChar][char]/p1[prevChar],"  ",p2Bi[prevChar][char] )
		prevChar=char
	#print(" " )

	print("monogram p(lang1)= ",prob1/(prob1+prob2) )
	print("monogram p(lang2)= ",prob2/(prob1+prob2) )
	print(" " )
	print("bigram   p(lang1)= ",prob1Bi/(prob1Bi+prob2Bi) )
	print("bigram   p(lang2)= ",prob2Bi/(prob1Bi+prob2Bi) )


# note this implementation would break down numerically if we calculate with long strings
# then we need to use logarithms and add instead

# note also that it is quite possible to shortcut p and only work with the frequencies directly
# the program would be simpler
# but I wanted to show how we conceptually create a probability model

# exactly how to handle the zero-frequency problem easily becomes a little mess...
# it can be improved or at least be made more consistent








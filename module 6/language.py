lang1file = open('lang1.txt','r',encoding="utf8")
lang1=lang1file.read()
lang2file = open('lang2.txt','r',encoding="utf8")
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

# now calculate the probability of the string for the two available models

string = input('Please enter a string!  ')
string = string.lower()

prob1=prob2=1
for c in string: prob1 *= p1[ord(c)]
for c in string: prob2 *= p2[ord(c)]

print("p(lang1)= ",prob1/(prob1+prob2) )
print("p(lang2)= ",prob2/(prob1+prob2) )

# note this implementation would break down numerically if we calculate with long strings
# then we need to use logarithms and add instead

# for now we assume only the simplest possible independent letter model
# if we were to use a markov chain model with bigrams the identification would be *much* sharper!





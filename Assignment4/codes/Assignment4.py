#Assignment-4
import collections
import numpy as np
import random
import matplotlib.pyplot as plt
import scipy

def CountFrequency(arr):
    return collections.Counter(arr)  
simlen = 100
x = np.linspace(0,150,100)
err = [] 
sr=[]
#Taking lambda = 5
s = np.random.poisson(5, simlen)
#count, bins, ignored = plt.hist(s, 14, density=True)
#plt.show()
for g in range(simlen):
  sr.append(s*s + 3)
for i in range(0,100):
	err_ind = np.nonzero(sr < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

freq = CountFrequency(s)
# iterate dictionary named as freq to print
# count of each element
freqArrayX = np.zeros(25)
freqArrayY = np.zeros(100)
for (key, value) in freq.items():
    print (key, " -> ", value)
    freqArrayX[key] = value
    if (key*key) + 3 < 100:
      freqArrayY[(key*key) + 3] = value
y = np.random.poisson(5,simlen)
freqArrayYExpFunc = CountFrequency(y)
freqArrayYExp = np.zeros(100)
for (key,value) in freqArrayYExpFunc.items():
    if (key*key) + 3 < 100:
      freqArrayYExp[(key*key) + 3] = value
plt.plot(x.T, err)
plt.show()

plt.stem(freqArrayY, markerfmt='o', use_line_collection=True, label = 'Simulated')
plt.stem(freqArrayYExp, markerfmt='o', use_line_collection=True, label = 'Theoretical')
plt.legend()
plt.grid()
plt.show()
plt.stem(freqArrayX, markerfmt='o', use_line_collection=True, label = 'X')
plt.legend()
plt.grid()
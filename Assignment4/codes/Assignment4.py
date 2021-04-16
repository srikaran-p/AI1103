import collections
import numpy as np
import random
import matplotlib.pyplot as plt

def CountFrequency(arr):
    return collections.Counter(arr)  
simlen = 10000

#Taking lambda = 5
s = np.random.poisson(5, simlen)
#count, bins, ignored = plt.hist(s, 14, density=True)
#plt.show()
freq = CountFrequency(s)
# iterate dictionary named as freq to print
# count of each element
freqArrayX = np.zeros(25)
freqArrayY = np.zeros(25)
for (key, value) in freq.items():
    print (key, " -> ", value)
    freqArrayX[key] = value
    if (key*key) + 3 < 25:
      freqArrayY[(key*key) + 3] = value

plt.stem(freqArrayX, markerfmt='o', use_line_collection=True, label = 'X')
plt.stem(freqArrayY, markerfmt='o', use_line_collection=True, label = 'Y')
plt.legend()
plt.grid()
# -*- coding: utf-8 -*-
"""Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PUfTH2GXpm2_UQQn7RoYqNLN1SSdDHs4
"""

import numpy as np
import matplotlib.pyplot as plt

simlen = 8

#0 is tails and 1 is heads
binary_array = np.zeros((8, 3))
#Generating the sample space using the binary representation from 0 to 7
print("The sample space (0 is tails and 1 is heads):")
for i in range(8):
    binary_string = format(i, "b")    
    length = len(binary_string)
    for j in range(0, 3-length):
        binary_array[i,j] = 0
    for j in range(3-length, 3):
        binary_array[i,j] = ord(binary_string[j-(3-length)]) - 48
    print(binary_array[i,:])

X_array = np.zeros(8)
#Filling the values in X_array with the given data
for i in range(8):
    sum = 0;
    for j in range(3):
        if binary_array[i,j] == 0:
            sum -= 1.5
        else:
            sum += 2
    X_array[i] = sum

print("Possible values of X given the sample space:")
print(X_array[:])
unique, counts = np.unique(X_array, return_counts=True)
psim = counts/simlen

plt.stem(unique,psim, markerfmt='o', use_line_collection=True, label='Simulation')
plt.xlabel('$X$')
plt.ylabel('$p(X)$')
plt.grid()
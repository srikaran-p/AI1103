import numpy as np
import random
import matplotlib.pyplot as plt
import math

simlen = 10000
x = [2,3,4,5,6,7,8,9,10]
count = [0,0,0,0,0,0,0,0,0]
for j in range(2,11):
  for i in range(simlen):
    random_matrix_array = np.random.randint(0,2,size=(j,j))
    det = np.linalg.det(random_matrix_array)
    if det > 0:
      count[j-2] = count[j-2] + 1

theoretical = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
theoreticalValue = 0.5;
for k in range(2,11):
  theoreticalValue = theoreticalValue * (1 - math.pow(2,-k));
  theoretical[k-2] = theoretical[k-2] * theoreticalValue

simulated = [0,0,0,0,0,0,0,0,0]
for i in range(0,9):
  simulated[i] = count[i] / simlen

#x = np.array([1, 1])
#y = np.array([P_X1_Y0, analysis_ans])
y1 = np.array(simulated)
y2 = np.array(theoretical)

print(theoretical)
print(simulated)
#plt.stem(unique,psim, markerfmt='o', use_line_collection=True, label='Simulation')
plt.ylim(0, 1)
#plt.xlim(2,10)
plt.stem(x,y1, markerfmt='o', use_line_collection=True, label = 'Simulation')
plt.stem(x,y2, markerfmt='o', use_line_collection=True, label = 'Theoretical')
plt.ylabel('$Pr($det $M > 0)$')
plt.xlabel('$n$')
plt.legend()
plt.grid()

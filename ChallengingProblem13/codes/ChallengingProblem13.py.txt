import numpy as np
import random
import matplotlib.pyplot as plt

simlen = 10000
count = 0
for i in range(simlen):
  random_matrix_array = np.random.randint(0,2,size=(4,4))
  det = np.linalg.det(random_matrix_array)
  if det > 0:
    count = count + 1

theoretical = 0.5 * ((15 * 14 * 12 * 8)/ (256 * 256))
simulated = count / simlen

x = np.array([1, 1])
y1 = np.array([simulated])
y2 = np.array([theoretical])

#plt.stem(unique,psim, markerfmt='o', use_line_collection=True, label='Simulation')
plt.ylim(0, 1)
plt.stem(y1, markerfmt='o', use_line_collection=True, label = 'Simulation')
plt.stem(y2, markerfmt='o', use_line_collection=True, label = 'Theoretical')
plt.ylabel('$Pr($det $M > 0)$')
plt.legend()
plt.grid()
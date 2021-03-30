import numpy as np
import random
import matplotlib.pyplot as plt
from google.colab import files

simlen = 10000
count = 0.0
theoretical = 0.85556
for i in range(simlen):
  value = random.randint(10, 99)
  if(value % 7 != 0):
    count = count + 1
simulated = count/simlen
print("Final answer (simluated): " + str(simulated))
print("Theoritical answer: " + str(theoretical))

x = np.array([1, 1])
y1 = np.array([simulated])
y2 = np.array([theoretical])

#plt.stem(unique,psim, markerfmt='o', use_line_collection=True, label='Simulation')
plt.ylim(0.8 , 0.9)
plt.stem(y1, markerfmt='o', use_line_collection=True, label = 'Simulation')
plt.stem(y2, markerfmt='o', use_line_collection=True, label = 'Theoretical')
plt.ylabel('Pr(X mod 7 != 0)')
plt.legend()
plt.grid()
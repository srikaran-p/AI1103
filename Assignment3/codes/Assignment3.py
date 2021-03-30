import numpy as np
import random
import matplotlib.pyplot as plt
from google.colab import files

simlen = 10000
theoretical = 2.25
x = np.array([0,1,2,11/3])
p = np.array([0.25, 1/12, 1/6, 0.5])

sample = np.random.choice(x, simlen, p=[0.25, 1/12, 1/6, 0.5])
sum = np.sum(sample)
simulated = sum/simlen

print("Final answer (simluated): " + str(simulated))
print("Theoritical answer: " + str(theoretical))

x = np.array([1, 1])
y1 = np.array([simulated])
y2 = np.array([theoretical])

#plt.stem(unique,psim, markerfmt='o', use_line_collection=True, label='Simulation')
plt.ylim(2.2 , 2.3)
plt.stem(y1, markerfmt='o', use_line_collection=True, label = 'Simulation')
plt.stem(y2, markerfmt='o', use_line_collection=True, label = 'Theoretical')
plt.ylabel('E(X)')
plt.legend()
plt.grid()
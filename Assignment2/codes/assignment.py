import numpy as np
import random
import matplotlib.pyplot as plt
from google.colab import files

def choose(p):
    return '1' if random.random() < p else '0'

simlen = 10000
#P_X1 = Pr(X = 1)
arr_P_X1 = [choose(0.8) for i in range(simlen)]
P_X1 = float(arr_P_X1.count('1'))/simlen 
print('Pr(X = 1) = ' + str(P_X1))

#P_X0 = Pr(X = 0)
P_X0 = 1 - P_X1

#P_Y0_X1 = Pr({Y = 0} | {X = 1})
arr_P_Y0_X1 = [choose(1.0/7.0) for i in range(simlen)]
P_Y0_X1 = float(arr_P_Y0_X1.count('1'))/simlen 
print('Pr({Y = 0} | (X = 1)) = ' + str(P_Y0_X1))

#P_Y0_X0 = Pr({Y = 0} | {X = 0})
arr_P_Y0_X0 = [choose(6.0/7.0) for i in range(simlen)]
P_Y0_X0 = float(arr_P_Y0_X0.count('1'))/simlen 
print('Pr({Y = 0} | (X = 0)) = ' + str(P_Y0_X0))

#P_Y0 = Pr(Y = 0) = Pr({Y = 0} | {X = 0})Pr(X = 0) + Pr({Y = 0} | {X = 1})Pr(X = 1)
P_Y0 = P_Y0_X0 * P_X0 + P_Y0_X1 * P_X1

#P_X1_Y0 = Pr({X = 1} | {Y = 0}). This is computed using eq. (0.0.4) in solution
P_X1_Y0 = (P_Y0_X1 * P_X1) / P_Y0
analysis_ans = 0.4
print("Final answer (simluated): " + str(P_X1_Y0))
print("Theoritical answer: " + str(analysis_ans))

x = np.array([1, 1])
#y = np.array([P_X1_Y0, analysis_ans])
y1 = np.array([P_X1_Y0])
y2 = np.array([analysis_ans])

#plt.stem(unique,psim, markerfmt='o', use_line_collection=True, label='Simulation')
plt.ylim(0.3 , 0.5)
plt.stem(y1, markerfmt='o', use_line_collection=True, label = 'Simulation')
plt.stem(y2, markerfmt='o', use_line_collection=True, label = 'Theoretical')
plt.ylabel('$Pr(\{X = 1\} | \{Y = 0\})$')
plt.legend()
plt.grid()
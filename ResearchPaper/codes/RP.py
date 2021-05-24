#Research Paper
import math
import numpy as np
import matplotlib.pyplot as plt

#kT = 0.1
k = 0.1
x4 = np.linspace(0, 1, 2048, endpoint = True)
y4 = (np.exp(x4/k) + np.exp((1-x4)/k)) / (1 + math.exp(1/k))
plt.plot(x4, y4)
plt.xlabel("$x_4$")
plt.ylabel("Pr($x_4$)")
plt.grid()
plt.show()

x5 = np.linspace(0, 1, 2048, endpoint = True)
y5 = (np.exp(x5/k) + 3*np.exp((1-x5)/k) + np.exp((1+x5)/k) + 3*np.exp((2-x5)/k))/(1 + 4*math.exp(1/k) + 3*math.exp(2/k))
plt.plot(x5, y5)
plt.xlabel("$x_5$")
plt.ylabel("Pr($x_5$)")
plt.grid()
plt.show()

x6 = np.linspace(0, 1, 2048, endpoint = True)
y6 = (28*np.exp((1+x6)/k) + 13*np.exp(x6/k) + 15*np.exp((2+x6)/k) + 3*np.exp((1-x6)/k) + 4*np.exp((2-x6)/k) + np.exp((3-x6)/k)) / (3 + 17*math.exp(1/k) + 29*math.exp(2/k) + 15*math.exp(3/k))
plt.plot(x6, y6)
plt.xlabel("$x_6$")
plt.ylabel("Pr($x_6$)")
plt.grid()
plt.show()

x7 = np.linspace(0, 1, 2048, endpoint = True)
y7 = (31*np.exp((1+x7)/k) + 19*np.exp((2+x7)/k) + np.exp((3+x7)/k) + 3*np.exp((1-x7)/k) + 17*np.exp((2-x7)/k) + 29*np.exp((3-x7)/k) + 15*np.exp((4-x7)/k)) / (34*math.exp(1/k) + 36*math.exp(2/k) + 30*math.exp(3/k) + 15*math.exp(4/k))
plt.plot(x7, y7)
plt.xlabel("$x_7$")
plt.ylabel("Pr($x_7$)")
plt.grid()
plt.show()

plt.plot(x7,y7,label = "kT = 0.1")
k = 0.2
y7 = (31*np.exp((1+x7)/k) + 19*np.exp((2+x7)/k) + np.exp((3+x7)/k) + 3*np.exp((1-x7)/k) + 17*np.exp((2-x7)/k) + 29*np.exp((3-x7)/k) + 15*np.exp((4-x7)/k)) / (34*math.exp(1/k) + 36*math.exp(2/k) + 30*math.exp(3/k) + 15*math.exp(4/k))
plt.plot(x7,y7,label = "kT = 0.2", linestyle= "-.")
k = 0.5
y7 = (31*np.exp((1+x7)/k) + 19*np.exp((2+x7)/k) + np.exp((3+x7)/k) + 3*np.exp((1-x7)/k) + 17*np.exp((2-x7)/k) + 29*np.exp((3-x7)/k) + 15*np.exp((4-x7)/k)) / (34*math.exp(1/k) + 36*math.exp(2/k) + 30*math.exp(3/k) + 15*math.exp(4/k))
plt.plot(x7,y7,label = "kT = 0.5", linestyle= "-")
plt.xlabel("$x_7$")
plt.ylabel("Pr($x_7$)")
plt.grid()
plt.legend()
plt.show()
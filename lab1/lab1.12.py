import numpy as np
import matplotlib.pyplot as plt
import random

N = 100000
m = 0
D = 2

x = []
for i in range (N):
    x.append(random.gauss(m, np.sqrt(D)))
    
plt.subplot(1, 1, 1)
plt.hist(x, bins = 40)
plt.xlabel('X')
plt.ylabel('Частота')

plt.show()
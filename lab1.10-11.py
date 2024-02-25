import numpy as np
import matplotlib.pyplot as plt

def generate_variable(bounds_x, bounds_y, N):
    x = np.random.uniform(bounds_x[0], bounds_x[1], N)  
    y = np.random.uniform(bounds_y[0], bounds_y[1], N)
    return x, y

bounds_x = (-2, 2)
bounds_y = (-3, 3)
N = 1000

x, y = generate_variable(bounds_x, bounds_y, N)


# график точек
plt.figure()
plt.scatter(x, y, color='b', alpha=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

# гистограммы распределения
plt.figure()

plt.subplot(1, 2, 1)
plt.hist(x, bins=20)
plt.xlabel('X')
plt.ylabel('Частота')
plt.title('Распределение X')

plt.subplot(1, 2, 2)
plt.hist(y, bins=20)
plt.xlabel('Y')
plt.ylabel('Частота')
plt.title('Распределение Y')

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

def generate_random_variable(bounds_x, bounds_y, num_samples):
    x = np.random.uniform(bounds_x[0], bounds_x[1], num_samples)
    y = np.random.uniform(bounds_y[0], bounds_y[1], num_samples)
    return x, y

# Задаем границы области изменения
bounds_x = (-5, 5)
bounds_y = (-3, 3)
num_samples = 1000

# Генерируем двумерную случайную величину
x, y = generate_random_variable(bounds_x, bounds_y, num_samples)

# Строим график точек
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='b', alpha=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Реализация двумерной случайной величины')
plt.grid(True)
plt.show()

# Строим гистограммы распределения компонент
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.hist(x, bins=20, color='b', alpha=0.7)
plt.xlabel('X')
plt.ylabel('Частота')
plt.title('Распределение X')

plt.subplot(1, 2, 2)
plt.hist(y, bins=20, color='b', alpha=0.7)
plt.xlabel('Y')
plt.ylabel('Частота')
plt.title('Распределение Y')

plt.tight_layout()
plt.show()

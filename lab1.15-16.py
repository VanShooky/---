import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1)
y = 2 * x**2 + x - 1
M = [x, y]
print(M)

# запись
fid = open('MyFile.txt', 'wt')

# заголовок
str = 'Значения функции y = 2*x^2 + x - 1'
fid.write(str + '\n')

for row in M:
    for element in row:
        fid.write('{:6.2f} '.format(element))
    fid.write('\n')
fid.close()

# Чтение

fid = open('MyFile.txt', 'r')
title = fid.readline().strip()
print(title)

A = []
for line in fid:
    A.append(list(map(float, line.split())))
fid.close()
print(np.transpose(A))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

line, = ax.plot(A[0], A[1])
ax.set_title(' y = 2*x^2 + x - 1')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xticks(np.linspace(x.min(), x.max(), 10))
ax.set_yticks(np.linspace(y.min(), y.max(), 10))

plt.show()



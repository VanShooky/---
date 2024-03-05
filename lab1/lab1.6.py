import numpy as np
from lab import print_matrix, fill_matrix

# Нахождение максимального и минимального элементов матрицы
C = np.zeros((5,5), int)
fill_matrix(C, 5, 5)
        
print_matrix(C)

print(C.max(axis = 0))
print(C.min(axis = 0))

print(C.max(axis = 1))
print(C.min(axis = 1))

print(C.max())
print(C.min())


        
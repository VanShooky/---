import numpy as np
from lab import print_matrix

# 1.1

result = ((5 + 3) * 2) / (7 - 1) + 10 % 3

print("Результат вычислений:", result)

# 1.2 там создание m файлов

# 1.3 
# ^ - возведение в степень
# Функция V = asin(Z) вычисляет обратную функцию синуса от значений элементов массива Z.
# Функция Y = inv(A) вычисляет матрицу, обратную квадратной матрице A.
# plot(y) – рисует зависимость y от номера если это вектор, или набор кривых, если – матрица (по столбцам от номера строки)

# 1.4 очистка экрана и рабочего пространства

# 1.5 вектор и матрица

vctr = np.array([1,2,3,4,5])
# print("Вектор: ", vctr)

matrix = [ [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]]

print_matrix(matrix)

# print(matrix[2])
# print(matrix[1][3])

matrix = np.insert(matrix,[2],[[10,10,10,10,10]], 0)
# print_matrix(matrix)

matrix = np.insert(matrix,[5],[[1],[2],[3],[4]], 1)
# print_matrix(matrix)

matrix = np.delete(matrix,[3],0)
# print_matrix(matrix)

matrix = np.delete(matrix,[5],1)
# print_matrix(matrix)



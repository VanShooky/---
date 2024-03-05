import random
import numpy as np
from lab import print_matrix, print_3D_arr, fill_3D_array, fill_matrix
from scipy.linalg import solve

arr_3D = np.zeros((2,3,4), int)            
                
fill_3D_array(arr_3D, 2, 3, 4)
print_3D_arr(arr_3D, 2, 3)    
         
print(arr_3D[1][1][3], "\n")

print(arr_3D.size, "\n")


matrix = np.zeros((3, 4), int)
fill_matrix(matrix, 3, 4)

print_matrix(matrix)

matrix_T = np.transpose(matrix)
print_matrix(matrix_T)

a = np.array([2, 3, 4, 5])
b = np.array([1, 2, 3, 4])

print(a + b, "\n")
print(a - b, "\n")
print(a / b, "\n")
print(a * b, "\n")
print(a**2, "\n")

str = 'pupupupu'
arr_str = {'pu', 'tu', 'du'}

A = [[2, 1],[3, 4]]
B = [[4],[11]]

print(solve(A, B))

import random
import numpy as np
from lab import print_matrix, print_3D_arr, fill_3D_array, fill_matrix

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

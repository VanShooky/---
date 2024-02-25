from lab import print_matrix, fill_matrix
import numpy as np

def sum(matrix):
    sum = 0
    for row in matrix:
        for element in row:
                sum += element
    return sum

n = 2
m = 3

Q = np.zeros((n,m), int)
fill_matrix(Q, n, m)
print_matrix(Q)
print(sum(Q))




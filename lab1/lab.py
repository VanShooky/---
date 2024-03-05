import random

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()
    print()    
        
def print_3D_arr(arr, n, m):
    for i in range(n):
        for j in range(m):
            print(arr[i][j])
        print()
    print()


def fill_3D_array(arr, n, m, p):
    for i in range(n):
        for j in range(m):
            for k in range(p):
                arr[i][j][k] = random.randint(0, 10)
                
def fill_matrix(arr, n, m):
     for i in range(n):
        for j in range(m):
                arr[i][j] = random.randint(0, 10) 

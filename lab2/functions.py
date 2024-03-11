import numpy as np

# 3
def func1(x,g):
    return x/(g**2) * np.exp(-((x**2)/2*(g**2)))

# 5
def func2(x,a,b):
    return (a/2)*np.exp(-a*(np.abs(x-b)))

# 6
def func3(x,l):
    return l*np.exp(-l*x)
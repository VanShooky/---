import numpy as np

def func3(x,g):
    return x/(g**2) * np.exp(-((x**2)/2*(g**2)))

def func5(x,g):
    a=0
    b=0
    return (a/2)*np.exp(-a*(np.abs(x-b)))

def func6(x,g):
    l = 5
    return l*np.exp(-l*x)
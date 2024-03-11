import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from functions import*
from scipy.stats import t

# чтение данных
data = np.loadtxt('lab2\data1.txt')
x = data[:, 0]
y = data[:, 1]
errors = data[:, 2]

# оптимизация
const1, cov_matrix1 = curve_fit(func1, x, y, sigma=errors)
const2, cov_matrix2 = curve_fit(func2, x, y, sigma=errors)
const3, cov_matrix3 = curve_fit(func3, x, y, sigma=errors)


# график
plt.plot(x, y, label='Экспериментальные данные')
plt.plot(x, func1(x, const1), label='функция 1')
plt.plot(x, func2(x, const2[0],const2[1]), label='функция 2')
plt.plot(x, func3(x, const3), label='функция 3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График экспериментальных данных')
plt.legend()
plt.show()


# Оценка качества анализа данных
x_sq = np.sum(((func1(x, const1) - y) / errors)**2) / (len(x) - 2)
print("χ^2 для функции 1:", x_sq)

x_sq = np.sum(((func2(x, const2[0],const2[1]) - y) / errors)**2) / (len(x) - 3)
print("χ^2 для функции 2:", x_sq)

x_sq = np.sum(((func3(x, const3) - y) / errors)**2) / (len(x) - 2)
print("χ^2 для функции 3:", x_sq)

R1 = (func1(x, const1) - y) / errors
R2 = (func2(x, const2[0], const2[1]) - y) / errors
R3 = (func3(x, const3) - y) / errors

plt.plot(x, R1, label='функция 1')
plt.plot(x, R2, label='функция 2')
plt.plot(x, R3, label='функция 3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График взвешенных остатков')
plt.legend()
plt.show()

def culc_A(N,k,R):
    A = np.zeros(k)
    for i in range (k):
        s1 = 0
        for j in range(N-i):
            s1 += R[j]*R[j+i] 
        s1/= N-i+1
        s2 = sum(R**2)/N
        A[i] = s1/s2   
    return A

N = 200
k = 75
k_arange = np.arange(0,75,1)
plt.plot(k_arange, culc_A(N,k,R1), label='функция 1')
plt.plot(k_arange, culc_A(N,k,R2), label='функция 2')
plt.plot(k_arange, culc_A(N,k,R3), label='функция 3')
plt.xlabel('k')
plt.ylabel('Ak')
plt.title('График автокорреляционной функции взвешенных остатков')
plt.legend()
plt.show()

# Построение 68% доверительных интервалов для оценок параметров
def conf_interval(confidence_level, constants, cov_matrix):
    t_value = t.ppf(confidence_level / 2, len(x) - 1)
    quantile = t_value * np.sqrt(np.diag(cov_matrix))
    return constants + quantile


print("Доверительный интервал функция 1:", conf_interval(1-0.68,const1,cov_matrix1), conf_interval(0.68,const1,cov_matrix1))
print("Доверительный интервал функция 2:", conf_interval(1-0.68,const2,cov_matrix2), conf_interval(0.68,const2,cov_matrix2))
print("Доверительный интервал функция 3:", conf_interval(1-0.68,const3,cov_matrix3), conf_interval(0.68,const3,cov_matrix3))




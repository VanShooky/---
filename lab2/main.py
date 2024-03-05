import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from functions import*

# Загрузка данных из файла
data = np.loadtxt('lab2\data1.txt')
x = data[:, 0]
y = data[:, 1]
errors = data[:, 2]


# Нелинейная аппроксимация данных
def fit_data(func, x, y, errors, initial_guess):
    optimal_params, cov_matrix = curve_fit(func, x, y, sigma=errors, p0=initial_guess)
    return optimal_params, cov_matrix

# Процедура НМНК анализа данных
initial_guess1 = [1.0]
theta1_opt, cov_matrix1 = fit_data(func3, x, y, errors, initial_guess1)

initial_guess2 = [1.0]
theta2_opt, cov_matrix2 = fit_data(func5, x, y, errors, initial_guess2)

initial_guess3 = [1.0]
theta3_opt, cov_matrix3 = fit_data(func6, x, y, errors, initial_guess3)

# Оценка качества анализа данных
chi_squared = np.sum(((y - func6(x, theta1_opt)) / errors)**2) / (len(x) - 1)
print("Нормированный критерий χ^2 для функции 1:", chi_squared)

# Построение графика данных и аппроксимирующей функции
plt.errorbar(x, y, yerr=errors, fmt='o', label='Экспериментальные данные')
plt.plot(x, func6(x, theta1_opt), label='Аппроксимирующая функция 1')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График экспериментальных данных и аппроксимирующей функции 1')
plt.legend()
plt.show()

# Построение 68% доверительных интервалов для оценок параметров
from scipy.stats import t

confidence_level = 0.68
t_value = t.ppf(1 - (1 - confidence_level) / 2, len(x) - 1)
theta1_interval = t_value * np.sqrt(np.diag(cov_matrix1))

print("Доверительный интервал для theta1:", theta1_opt - theta1_interval, theta1_opt + theta1_interval)





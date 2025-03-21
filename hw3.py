import math
import numpy as np
import matplotlib.pyplot as plt

# Exponential function f(x) = e^x
def f(x):
    return np.exp(x)
# Function to evaluate Newton's interpolating polynomial
def newton_polynomial(coefficient, x_data, x):
    n = len(coefficient)
    polynomial = coefficient[0]
    term = 1.0
    for i in range(1, n):
        term *= (x - x_data[i - 1])
        polynomial += coefficient[i] * term
    return polynomial
# Function to calculate divided differences
def divided_differences(x, y):
    n = len(x)
    coef = np.zeros([n, n])
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i, j] = (coef[i + 1, j - 1] - coef[i, j - 1]) / (x[i + j] - x[i])
    return coef[0, :]

# Function to compute Newton polynomial and error for f(x) = e^x for the given n values = [2,4,8,16,32] 
def newton_poly(f, n_vals, against=501):
    errors = []
    x_list = np.linspace(-1, 1, against)
    f_samples = f(x_list)
    for n in n_vals:
        x_nodes = np.linspace(-1, 1, n + 1)
        y_nodes = f(x_nodes)
        # here we get the divided difference coefficients for the corresponding x and y nodes
        coef = divided_differences(x_nodes, y_nodes)
        # here we evaluate the polynomial at the calculated sample points 
        p_samples = np.array([newton_polynomial(coef, x_nodes, x) for x in x_list])
        # here we compute the error
        error = abs(f_samples - p_samples)
        max_error = max(error)
        errors.append(max_error)
    
    return errors, n_vals

# given n values in the problem 
n_values = [2, 4, 8, 16, 32]

# Compute errors for newton interpolation 
error_list, n_values = newton_poly(f, n_values)
for i in range(len(error_list)):
    print("max error calculated for n = ",n_values[i], " => ", error_list[i])

# graphing the error calculated vs n values
plt.figure(figsize=(8, 6))
plt.plot(n_values, error_list, marker='o', linestyle='-', color='b', label='Error')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('n')
plt.ylabel('Max Error')
plt.title('Max error vs. n graph')
plt.legend()
plt.grid(True)
plt.show()

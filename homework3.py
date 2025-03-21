import math
import numpy as np
import matplotlib.pyplot as plt
#function to calculate the n+1 interpolating points xi for 0<= i <= n 
def points(n):
    x = [0]*(n+1)
    for i in range(n+1):
        h =  ((2)/(n))
        x[i] = h*i + (-1)
    return x

#function to calculate the value of the given function f(x) = e^x
def f(x_points):
    y_points = [0]*len(x_points)
    for i in range(len(y_points)):
        y = math.exp(x_points[i])
        y_points[i] = y

    return y_points

#function to calculate the n degree polynomial 
def newton_poly(x, x_list, coefficient_list):
    n = len(coefficient_list)
    polynomial = coefficient_list[0]
    term = 1
    for i in range(1,n):
        term *= (x- x_list[i-1])
        polynomial += coefficient_list[i]*term
    return polynomial
    

# #function to calculate the coefficients 
def coefficients(x_list_i, y_list_i):
   n = len(y_list_i)
   coefficients_list = np.copy(y_list_i)
   for j in range(1,n):
    for i in range(n-1, j-1, -1):
        coefficients_list[i] = (coefficients_list[i]-coefficients_list[i-1])/(x_list_i[i]-x_list_i[i-j])
    
    return coefficients_list
   
list = [2,4,8,16,32]
x_list = [[0]*3, [0]*5, [0]*9, [0]*17, [0]*33]
#here we have the list of x points list
for i in range(len(list)):
    x_list[i] = points(list[i])    
    #print(i, " ", x_list[i])    

#here we get the corresponding y points for the x values for the function
y_list = [0]*len(x_list)
for i in range(len(x_list)):       
    y_list[i] = f(x_list[i])
    #print(i," ",y_list[i])

#here we get the coefficients for each of the x and y values for the corresponding n values
coefficient_list = [[0]*3, [0]*5, [0]*9, [0]*17, [0]*33]
for i in range(len(x_list)):
    coeff = coefficients(x_list[i], y_list[i])
    coefficient_list[i] = coeff
    
#here we get the polynomial value calculated at a given input value of x
polynomial_list = [0]*5
for i in range(len(x_list)):
    x = 0.5 #calculating at x = 0.5 for example
    polynomial = newton_poly(x,x_list[i],coefficient_list[i])
    polynomial_list[i] = polynomial
    #print(i," ",polynomial)

def calc_max(interpolating_points):
    maxi = abs(interpolating_points[0] - interpolating_points[1])
    for i in range(2,len(interpolating_points)):
        if(abs(interpolating_points[i]-interpolating_points[i-1]) > maxi):
            maxi = abs(interpolating_points[i]-interpolating_points[i-1])
    return maxi


errors = [0]*len(list)
#computing error
for i in range(len(list)):
    #since the derivative of e^x is same everytime M = max(e^x) = e
    m = math.exp(1)
    interpolating_points = points(list[i])
    #h= (1-(-1))/n => 2/n
    h = 2/list[i]
    error = abs(m*math.pow(h, (list[i]+1)))/(4*(list[i]+1))
    errors[i] = error
    print(list[i], " ", error)


plt.plot(list, errors, marker='o')
plt.xlabel('n')
plt.ylabel('Maximum Error $E_n$')
plt.title('Maximum Error $E_n$ versus $n$')
plt.grid(True)
plt.show()
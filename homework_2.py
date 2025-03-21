import math
def bisection_method():
    iteration = 1
    a = 0.02
    b = 0.03
    print(a, ",",b, "=> input values of a and b")
    f_a = f(a)
    f_b = f(b)
    while(abs(b-a) >= math.pow(10,-6)):

        c = (a+b)/2
        f_c = f(c)
        if(f_c == 0):
            print(iteration ,  " => total iterations using bisection method" )
            print(abs(f_b - f_a) , " => error using bisection method")
            return c
        elif f_a * f_c < 0:
            b = c
        else:
            a = c
        iteration+=1
    
    print(iteration ,  " => total iterations using bisection method" )
    print(abs(f_b - f_a) , " => error using bisection method")
    return (a+b)/2

def f(r):
    return 150000 - (7200/r)*(1-math.pow((1+(r/12)), -360))

x_n = bisection_method()
print(x_n , "=> rate")
import math
#function to calculate the function result at x 
# i+1 is the question number on the homework
def f(x,i):
    match i:
        case 0: 
            return 1-(2*x*math.exp(-x/2))
        
        case 1: 
            return 5 - (math.pow(x, -1))
        
        case 2:
            return math.pow(x,3) - (2*x) - 5
        
        case 3: 
            return math.exp(x) - 2
        
        case 4: 
            return x - math.exp(-x)
        
        case 5:
            return math.pow(x,6) - x -1
        
        case 6:
            return math.pow(x,2) - math.sin(x)
        
        case 7: 
            return math.pow(x,3) - 2
        
        case 8: 
            return x + math.tan(x)
        
        case 9: 
            #print(x, " => value of x")
            return 2 - (math.log(x)/x)

#function to calculate the derivative of function at value x
# i+1 is the question number on the homework
def numerical_derivative( x,i):
    #print(x, " => value of x to be passed in the derivative")
    if(x<0):
        return 
    match i:
        case 0: 
            return -2*math.exp(-x/2) + x*math.exp(-x/2)
        case 1: 
            return math.pow(x,-2)
        case 2:
            return (3*math.pow(x,2)) - 2
        case 3:
            return math.exp(math.pow(x,2)) 
        case 4:
            return 1+math.exp(math.pow(x,-1))
        case 5:
            return (6*math.pow(x,5)) - 1
        case 6:
            return (2*x) - math.cos(x)
        case 7:
            return 3*math.pow(x,2)
        case 8:
            return 1+ (math.pow((1/math.cos(x)),2))
        case 9: 
            if(x<=0):
                #print( "f(x) = 2 - ln(x)/x does not have real roots because the value of f(x) never crosses x-axis because the value of x is out of the domain of the function.")
                return
            return ((math.log(x)-1)/math.pow(x,2))

#newton's method
#i+1 is the question number on the homework
def newton_method(x0,i):
    #calculate the derivative to check if it is greater than 0 (required to determine if the function will ever converge)
    derivative = numerical_derivative( x0,i)
    
    if(derivative == 0):
        return "newton_method() failed to converge from the initial guess"
    
    else:
        #calculating the root
        x_n = (x0) - (f(x0,i)/( derivative))
        iteration = 1
        while(abs(x_n - x0) >= math.pow(10,-6)):
            x0 = x_n
            if(x0<0):
                return 
            derivative =  numerical_derivative( x0,i)
            x_n = (x0) - ((f(x0,i))/(derivative))
            iteration +=1
        
    print(iteration, "=> total iterations using newton's method")
    print(abs(x_n - x0) , "=> error using newton's method")
    return x_n

#secant method
#i+1 is the question number on the homework
def secant_method(x0, x1,i):
    iteration = 1
    x_n = x1 - (f(x1,i)/ (((f(x1,i)) - (f(x0,i)))/ (x1-x0)))
    #print(x_n)
    while(abs(x_n - x1) >= math.pow(10,-6)):
        x0 = x1
        x1 = x_n
        x_n = x1 - (f(x1,i)/ (((f(x1,i)) - (f(x0,i)))/ (x1-x0)))
        iteration += 1

    print(iteration , "=> total iterations using secant method ")
    print(abs(x_n - x1) , "=> error using secant method")
    return x_n

#bisection method
#i+1 is the question number on the homework
def bisection_method(a,i):
    iteration = 1
    f_a = (f(a,i))
    b = get_Fb0(i)
    print(a, ",",b, "=> input values of a and b")
    f_b = f(b,i)
    while(abs(b-a) >= math.pow(10,-6)):
        c = (a+b)/2
        f_c = f(c,i)
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

# initial values of b determined by graphing the function
def get_Fb0(i):
    match i:
        case 0:
            return 1
        case 1: 
            return 0.1667
        case 2:
            return 2.1
        case 3:
            return 0.5
        case 4:
            return 0.3
        case 5:
            return 1.2
        case 6:
            return 1
        case 7:
            return 1.3
        case 8:
            return 1.5
        case 9:
            return 2

        
#list of initial guesses as given on the homework
list = [0, 1/4, 2, 1, 1, 1, 1/2, 1, 3, 1/3]

#calculated outputs
i = 0
while(i<=9):
    print("Problem:", i+1)
    print(list[i],"=> input")
    x_n = newton_method(list[i],i)
    if(x_n == None):
        print( "f(x) = 2 - ln(x)/x does not have real roots for problem ", i+1," because the value of f(x) never crosses x-axis.")
        print(" ")
        break
                
    else:
        print(x_n, " => output x_n using newton's method" )
        print(" ")

    print(list[i],"=> input")
    x_s = secant_method(list[i],list[i]+0.1,i) 
    print(x_s , " => output x_n using secant method")
    print(" ")

    x_b = bisection_method(list[i],i)
    print(x_b , " => output x_n using bisection method")
    print(" ")
    i+=1
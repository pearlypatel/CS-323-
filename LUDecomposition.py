a = [[14,14,-9,3,-5],
     [14,52,-15,2,-32],
     [-9,-15,36,-5,16],
     [3 ,2 ,-5 ,47 ,49],
     [-5,-32,16,49,79]]
# print(a[0][0])
b = [[-15],[-100],[106],[329],[463]]

def factorization(a, n ):
     L = [[0 if i!=j else 1 for j in range(n)] for i in range(n)]
     U = [[a[i][j] for j in range(n)] for i in range(n)]

     for k in range(n):
          if(U[k][k]==0):
               return

          for i in range(k+1, n):
               L[i][k] = (U[i][k])/(U[k][k])
          
               for j in range(k, n):
                    U[i][j] = U[i][j] - L[i][k]*U[k][j]                
     
     return L,U

L,U = factorization(a,5)

#solving for y values using the L matrix and b values given in the question
def forward_sub(L,b):
     y = [0]*len(L)
     for i in range(len(L)):
          y[i] = b[i][0]
          for j in range(i):
               y[i] -= L[i][j]*y[j]
          y[i] = y[i]/L[i][i]

     return y

#solving for x values using the U matrix and y values 
def backward_sub(U, y):
     x= [0]*len(U)
     for i in range(len(U)-1, -1, -1):
          x[i] = y[i]
          for j in range(i+1, len(U)):
               x[i] -= U[i][j]*x[j]
          x[i] = x[i]/U[i][i]

     return x

y = forward_sub(L, b)
x= backward_sub(U,y)
for i in range(len(x)):
     print("x_",i+1, " => ", x[i])
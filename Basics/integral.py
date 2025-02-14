#Calculation of the integral in Python for function x**3 + 1 in x range (1,3)
def integral(a, b, n, f):
    delta_x = (b - a) / n
    total = 0
    
    for i in range(1, n+1):
        middle_point = 0.5 * (2 * a + delta_x * (2*i - 1))
        total += f(middle_point)
        
    return total * delta_x

def function(x):
    return x**3 + 1

area = integral(a=1, b=3, n=1000, f=function)
print(area)


#Calculation of the integral in SymPy for function 3*x**2 + 1 in x range (0,2)
from sympy import *

x = symbols ('x')
#function 3*x**2 + 1
func = 3*x**2 + 1

#range x = 0 to 2
area_2 = integrate(func, (x, 0, 2))
print(area_2)
from sympy import *
from math import *

#exponentation
x = symbols('x')
exponentation = 8**(1/3) / 64**(1/3)
print(exponentation)

#compound interest
p = 100
r = 0.15
t = 2.0
m = 12
a = p * (1 + (r/m))**(m * t)
print(a)

#logarithm
y = log(64, 2)
print(y)

#natural logarithm
z = log(100)
print(z)

#limit functions
k = symbols('k')
f = 1/k 
result = limit(f, k, oo)
print(result)

#Euler's number
n = symbols('n')
f_2 = (1 + (1/n))**n
result_2 = limit(f_2, n, oo)
print(result_2)
print(result_2.evalf())


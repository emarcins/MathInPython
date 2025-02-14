from sympy import *

#using limits to calculate derivatives for func y=x**3 where x=2
x, s = symbols('x s')
f = x**3

derivative_f = (f.subs(x, x + s) - f) / ((x + s) - x)
derivative_x_is_2 = derivative_f.subs(x, 2)

result = limit(derivative_x_is_2, s, 0)

print(result)
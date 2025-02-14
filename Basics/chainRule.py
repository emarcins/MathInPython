from sympy import *


#Compoute derivative dz/dx with using CHAIN RULE and without CHAIN RULE

x, y = symbols('x y')
#first function and derivative
_y = x**2 + 1
dy_dx = diff(_y)
#second function and derivative
z = y**3 - 2
dz_dy = diff(z)
#compoute with chain rule
dz_dx_with_rule = (dz_dy * dy_dx).subs(y, _y)
#compoute without chain rule
dz_dx_without_rule = diff(z.subs(y, _y))

#both methods give the same results
print(dz_dx_with_rule)
print(dz_dx_without_rule)

#derivative dz/dx for x=2
print(dz_dx_with_rule.subs(x, 2))

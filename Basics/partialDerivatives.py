from sympy import *
from sympy.plotting import plot3d

#partial derviatives for (x,y) = (1,2)
x,y = symbols('x y')
f = 2*x**3 + 3*y**3
dx_f = diff(f, x)
dy_f = diff(f, y)

print(dx_f)
print(dy_f)

print(dx_f.subs(x,1))  
print(dy_f.subs(y,2))  

plot3d(f)

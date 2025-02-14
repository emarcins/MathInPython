#summing
x = [1,2,3,4,5]
summing = sum(2*i for i in x )
print(summing)

summing_2 = sum(2*i for i in range(1,6))
print(summing_2)

k = [2,1,3,7]
n = len(k)
l = int(input("Enter the number: "))

summing_3 = sum(l*k[i] for i in range(0, n))
print(summing_3)

#summing in SymPy
from sympy import *

i, m = symbols("i m")
summing_4 = Sum(2*i, (i, 1, m))
summing_to_10 = summing_4.subs(m, 10)
print(summing_to_10.doit())
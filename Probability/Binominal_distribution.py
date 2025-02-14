#Binomial distribution in Python (binomial distribution of Bernoulli)
"""
P = (n, k) * (p**k) * (1-p)**(n-k)

Where:
    (n,k) = n!/((n-k)! * k!
    k! = 1 * 2 * 3 * ... * k
    
n = number of attempts
k = number of successes
p = probability of success
"""

#1st step - factorial function
def factorial(n: int):
    f = 1
    for i in range(n):
        f *= (i + 1)
    return f

#2nd step - binomial coefficient(Newton's symbol)
def binomial_coefficient(n: int, k: int):
    return factorial(n) / (factorial(n - k) * factorial(k))

#3rd step - binomial distribution formula
def binominal_distribution(k: int, n: int, p: float):
    return binomial_coefficient(n, k) * (p**k) * (1-p)**(n-k)

#10 attempts, with 80% probability of success
n = 10
p = 0.8

for k in range(n + 1):
    probability = binominal_distribution(k, n, p)
    print("{Success} - {Probability}".format(Success=k, Probability=probability))
    
    
print("\n-----------------------\n")


#Binomial distribution in SciPy
from scipy.stats import binom

n = 10
p = 0.8

for k in range(n + 1):
    probability_two = binom.pmf(k, n, p)
    print("{Success} - {Probability}".format(Success=k, Probability=probability_two))
    
    
    
    
    
    
    
    
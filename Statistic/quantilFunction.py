#Normal distribution with Quantile function (in Polish: Dystrybuanta odwrotna) in Python and SciPy using func erfinv (in SciPy).
import random
from  scipy.special import erfinv

def normal_quantil_cdf(p: float, arith_mean: float, deviation: float):
    return arith_mean + (deviation * (2.0 ** 0.5) * erfinv((2.0 * p) - 1.0))

arith_mean = 29.15
deviation = 1.25

for i in range(0,100):
    random_probability = random.uniform(0, 1)
    print(normal_quantil_cdf(random_probability, arith_mean, deviation))
"""
Script draw 100 random probability numbers with arithmetic mean 29.15 and
standard deviation 1.25 and using normal distribution with quantil function in Python
(function erfinv in SciPy module) gives 100 random numbers.
"""

print("---------------")


#Normal distribution with Quantile function (in Polish: Dystrybuanta odwrotna) in SciPy called ppf - percent point function.
from scipy.stats import norm

arith_mean_2 = 29.15
deviation_2 = 1.25

x = norm.ppf(0.95, arith_mean_2, deviation_2)
print(x) # 31.206067033689337 = 31.21

"""
Normal distribution using SciPy percent point function (ppf) using
quantil function with arithmetic mean 29.15 and standard deviation 1.25 for
probability = 95% counting that 'x' value is equal to 31.21
"""


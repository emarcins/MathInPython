#Beta distribution in SciPy
from scipy.stats import beta

#Probability of 8 success in 10 attempts for probability of success < or = 90%
a = 8
b = 2

probability = beta.cdf(0.90, a, b)
print(probability) #0.7748409780000002

#Probability of 8 success in 10 attempts for probability of success > or = 90%
probability_two = 1.0 - beta.cdf(0.90, a, b)
print(probability_two) #0.22515902199999982

#Probability of 8 success in 10 attempts for probability of success >= 80% and <=90%
probability_three = beta.cdf(0.90, a, b) - beta.cdf(0.80, a, b)
print(probability_three) #0.33863336199999994


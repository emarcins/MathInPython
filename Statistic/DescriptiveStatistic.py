#Arithmetic mean
x = [1,3,2,7,4,2,9]

arithmetic_mean = sum(x) / len(x)
print(arithmetic_mean) # 4.0

#Weighted arithmetic mean
assessments = [0.90, 0.80, 0.65, 0.82]
weights = [0.2, 0.2, 0.2, 0.5]

weighted_arithmetic = sum(i * k for i,k in zip(assessments, weights)) / sum(weights)
print(weighted_arithmetic) # 0.8

#Median
y = [3,9,0,5,12,15]
print(sorted(y)) # [0, 3, 5, 9, 12, 15]

def median(y):
    sorted_y = sorted(y)
    n = len(sorted_y)
    if n % 2 == 0:
        return (sorted_y[int(n / 2 - 1)] + sorted_y[int(n / 2)]) / 2
    else:
        return sorted_y[int(n / 2)]


print(median(y)) # 7.0

#Standard deviation(SD)
from math import sqrt

data = [0, 2, 5, 8, 9, 12, 15]

def variance(values):
    arithm_mean = sum(values) / len(values)
    _variance = sum((v - arithm_mean) ** 2 for v in values) / len(values)
    return _variance

def standard_deviation(values):
    return sqrt(variance(values))

print(standard_deviation(data)) # 4.948716593053935

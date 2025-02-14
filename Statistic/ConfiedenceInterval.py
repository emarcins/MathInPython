#Confiedence interval
from math import sqrt
from scipy.stats import norm


#Counting Z-scores
def z_scores_for(p):
    #Scaling of the normal distribution to mean 0 and standard deviation 1 in norm_dist variable.
    norm_dist = norm(0.0, 1.0)
    left_tail= (1.0 - p)/ 2.0 #0 to 0.025
    right_tail = 1.0 - ((1.0 - p) / 2) #0.975 to 1.0
    return norm_dist.ppf(left_tail), norm_dist.ppf(right_tail)

print(z_scores_for(p=0.95)) #(-1.959963984540054, 1.959963984540054)

"""
Error margin formula:
    E = +-Z_score * (s / ( n ** 1/2))
    or using math module
    E = +-Z_score * (s / sqrt(n))    
    
    Where:
        E = error margin
        Z_score = Z-scores values
        s = standard deviation
        n - sample 
"""
def confiedence_interval(probability, sample_mean, s, n ):
    #Value of n(sample) has to be greater than 30!
    low, high = z_scores_for(probability)
    low_error = low * (s / sqrt(n))
    high_error = high * (s / sqrt(n))
    
    return sample_mean + low_error, sample_mean + high_error

print(confiedence_interval(probability=0.95, sample_mean=29.214, s=1.37, n=31)) #(28.73173270493526, 29.696267295064736)

"""
It means: For sample value = 31, with sample mean = 29.214 and standard deviation = 1.37,
I'm sure for 95% that population mean(and confiedence interval - in polish "przedział ufności") is in range 
from 28.732 to 29.696. 
Which it means that error margin(E) is equal to -0.48227 and 0.48227.
"""

print("---------------------------")


#Student's t-distribution - use for equal or smaller value of sample than 30
"""
Example of t-distribution in Scipy module. It prints Z-scores for 95% confiedence (left tail from 0 to 0.025 and 
right tail from 0.975 to 1.0) and value of sample(n) = 20.
"""
from scipy.stats import t

n = 20
left_tail_two = t.ppf(0.025, df=n-1)
right_tail_two = t.ppf(0.975, df=n-1)
#parameter "df=n-1" is degrees of freedom, which should one less than sample(n)

print("Z-scores for t-distribution(n=20)  and 95% confiedence interval are:",left_tail_two, "and:", right_tail_two)







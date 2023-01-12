# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
import math

max_load=float(input())
n=float(input())
mean=float(input())
sigma=float(input())
#print(max_load, n, mean, sigma)
#x=200

test=statistics.NormalDist(mean*n,sigma*math.pow(n,0.5))
print(round(test.cdf(max_load),4))

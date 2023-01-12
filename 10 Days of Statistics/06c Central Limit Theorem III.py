# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
import math

n=float(input())
mean=float(input())
sigma=float(input())
conf=float(input())
zscore=float(input())
#print(n, mean, sigma, conf, zscore)

lower=mean-zscore*sigma*math.pow(100,-0.5)
upper=mean+zscore*sigma*math.pow(100,-0.5)
print(round(lower,2))
print(round(upper,2))

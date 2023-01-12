# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics

mean, sd=map(float, input().split())
lowerbound=float(input())
low, high=map(float, input().split())

test=statistics.NormalDist(mean, sd)
print(round(test.cdf(lowerbound),3))
print(round(test.cdf(high)-test.cdf(low),3))

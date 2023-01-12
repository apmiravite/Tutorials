# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics

mu, sigma=map(float, input().split())
high=float(input())
passing=float(input())
#print(mu, sigma, high, passing)

test=statistics.NormalDist(mu,sigma)
print(round((1-test.cdf(high))*100,2))
print(round((1-test.cdf(passing))*100,2))
print(round(test.cdf(passing)*100,2))

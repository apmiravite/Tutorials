# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

lambda_=float(input())
value=int(input())
#print(lambda_)
#print(value)

def poisson(k,mean):
    return (math.pow(mean,k)*math.pow(math.e,-mean))/math.factorial(k)

print(round(poisson(value,lambda_),3))

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

p, n=map(int, input().split())
#print(n)

p=p/100
#print(p)

def binomialDist(k,n,p):
    return math.comb(n,k)*math.pow(p,k)*math.pow(1-p,n-k)

K=2
prob1=0    
for i in range(K+1):
    prob1=prob1+ binomialDist(i,n,p)
print(round(prob1,3))

prob2=0
for i in range(K):
    prob2=prob2+ binomialDist(i,n,p)
print(round(1-prob2,3))

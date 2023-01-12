# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

boys, girls = map(float, input().split())
#print(boys)
#print(girls)

pb=boys/(boys+girls)
pg=1-pb
#print(pb)
#print(pg)

def binomialDist(k,n,p):
    return math.comb(n,k)*math.pow(p,k)*math.pow(1-p,n-k)

N=6
K=3
prob=0
for i in range(K):
    #probability from 0 to K-1
    prob=prob+ binomialDist(i,N,pb)
#get the complement
print(round(1-prob,3))

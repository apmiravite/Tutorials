# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics
from sys import stdin

n=int(input())
X = list(map(float, stdin.readline().strip().split()))
Y = list(map(float, stdin.readline().strip().split()))
#print(n)
#print(X)
#print(Y)

sd_x=statistics.pstdev(X)
sd_y=statistics.pstdev(Y)
#print(sd_x)
#print(sd_y)

mu_x=statistics.mean(X)
mu_y=statistics.mean(Y)
#print(mu_x)
#print(mu_y)

cov=0
for i in range(n):
    cov=cov + (X[i]-mu_x)*(Y[i]-mu_y)*1/n
#print(corr)

pearson=cov/(sd_x*sd_y)
print(round(pearson,3))

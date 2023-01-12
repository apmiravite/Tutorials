# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 
n,d=map(int, input().split())
#print(n)
#print(d)

failure=n/d
success= 1-failure
#print(failure)

x=int(input())
#print(x)
prob=0
for i in range(x):
    prob=prob+math.pow(success,i)*failure

print(round(prob,3))

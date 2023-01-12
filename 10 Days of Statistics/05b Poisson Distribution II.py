# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

A, B= map(float, input().split())
#print(A)
#print(B)

# recall for poisson dist, E(X)=Var(X)=lambda
# Var(X)=E(X^2)-E(X)^2 -> E(X)=E(X^2)-E(X)^2
# E(X^2)=E(X)^2 + E(X)

cost_A=160+ 40*(math.pow(A,2)+A)
cost_B=128+ 40*(math.pow(B,2)+B)

print(format(cost_A,'.3f'))
print(format(cost_B,'.3f'))

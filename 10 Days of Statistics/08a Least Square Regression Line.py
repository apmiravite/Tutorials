# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics as s

n=5
x=[]
y=[]
for i in range(n):
    a, b=map(int, input().split())
    x.append(a)
    y.append(b)
#print(x)
#print(y)

def pearson(a, b):
    sd_a=s.pstdev(a)
    sd_b=s.pstdev(b)
    #print(sd_x)
    #print(sd_y)
    
    mu_a=s.mean(a)
    mu_b=s.mean(b)
    #print(mu_a)
    #print(mu_b)
    
    cov=0
    for i in range(n):
        cov=cov + (a[i]-mu_a)*(b[i]-mu_b)*1/n
    #print(cov)
    
    pearson_coef=cov/(sd_a*sd_b)
    #print(pearson_coef)
    return pearson_coef

beta= pearson(x,y)*s.pstdev(y)/s.pstdev(x)
#print(beta)

epsilon=s.mean(y)-beta*s.mean(x)
#print(epsilon)

def predict(b,e,x):
    y_hat=e+b*x
    print(round(y_hat,3))

predict(beta, epsilon, 80)

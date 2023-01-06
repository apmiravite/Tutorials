# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())


for i in range(0,N):
    String = input()
    print(String[0::2]+" "+String[1::2])  

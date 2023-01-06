# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(input())

directory ={}

for i in range(x):
    text=input().split()
    directory[text[0]]=text[1]
while True:
    try:
        query=input()
        if query in directory:
            print(query+"="+directory[query])
        else:
            print("Not found")
    except EOFError:
        break

# Enter your code here. Read input from STDIN. Print output to STDOUT
return_date=input()
return_array= list(map(int, return_date.split()))
due_date=input()
due_array=list(map(int, due_date.split()))
fine=0

if due_array[2]<return_array[2]:
    fine=10000
elif due_array[1]<return_array[1] and due_array[2]==return_array[2]:
    fine=500*(return_array[1]-due_array[1])
elif due_array[0]<return_array[0] and due_array[1]==return_array[1] and due_array[2]==return_array[2]:
    fine=15*(return_array[0]-due_array[0])
else:
    fine=0

print(fine)

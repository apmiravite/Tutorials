# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics

n=int(input())
arr = list(map(int, input().split()))
print(statistics.mean(arr))
print(statistics.median(arr))
print(statistics.mode(sorted(arr)))

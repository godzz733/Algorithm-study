import sys
input = sys.stdin.readline
n = int(input())
arr= []
count = 0
for _ in range(n):
    arr.append(int(input()))

for i in range(n-1,0,-1):
    while arr[i]<=arr[i-1]:
        arr[i-1] -=1
        count+=1

print(count)

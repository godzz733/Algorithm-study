import sys
input = sys.stdin.readline

a, b = map(int,input().rstrip().split())
arr = []
for i in range(1,1001):
    for k in range(i):
        arr.append(i)

result = 0
for i in range(a-1,b):
    result += arr[i]
print(result)


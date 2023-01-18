import sys
t = int(input())
arr =[]
for _ in range(t):
    a, b = map(int,sys.stdin.readline().split())
    arr.append([a,b])

arr.sort()
[print(i[0], i[1]) for i in arr]
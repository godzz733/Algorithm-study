import sys; input = sys.stdin.readline
from collections import deque

n,s,m = map(int,input().split())
v = [*map(int,input().split())]

arr = [[0] * (m+1) for _ in range(n+1)]
arr[0][s] = 1
for i in range(1,n+1):
    for j in range(m+1):
        if arr[i-1][j]:
            if j+v[i-1] <= m:
                arr[i][j+v[i-1]] = 1
            if j-v[i-1] >= 0:
                arr[i][j-v[i-1]] = 1

for i in range(m,-1,-1):
    if arr[n][i]:
        print(i)
        break
else:
    print(-1)
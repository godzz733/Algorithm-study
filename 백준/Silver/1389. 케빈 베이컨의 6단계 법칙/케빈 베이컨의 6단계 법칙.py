import sys
input = sys.stdin.readline
n,m = map(int,input().split())
INF = int(1e9)
arr = [[INF] * (n+1) for _ in range(n+1)]
result = []
for _ in range(m):
    a, b = map(int,input().split())
    arr[a][b] = 1
    arr[b][a] = 1
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            arr[a][b] = min(arr[a][b],arr[a][k]+arr[k][b])
for i in range(n+1):
    for k in range(n+1):
        if arr[i][k]== INF:
            arr[i][k] = 0
for i in arr:
    result.append(sum(i))
print(result.index(min(result[1:])))

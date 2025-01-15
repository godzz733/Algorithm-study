import sys; input = sys.stdin.readline
n,m,k = map(int,input().split())
arr = [[0] * (k+1) for _ in range(m+1)]
arr[m][k] = 0
for _ in range(n):
    a,b = map(int,input().split())
    for i in range(m,a-1,-1):
        for j in range(k,b-1,-1):
            arr[i][j] = max(arr[i][j],arr[i-a][j-b]+1)
ans = 0
for i in range(m+1):
    ans = max(arr[i])
print(ans)
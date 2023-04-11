def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

n, m, k = map(int,input().split())
arr = [*map(int,input().split())]
parent = [0] * (n+1)
dp = [int(1e9)] * (n+1)
result = 0
for i in range(1,n+1):
    parent[i] = i
for _ in range(m):
    a, b = map(int,input().split())
    union_parent(a,b)
for i in range(1,n+1):
    x = find_parent(i)
    dp[x] = min(dp[x], arr[i-1])
for i in range(1,n+1):
    if dp[i] != int(1e9):
        result += dp[i]
if result > k:
    print('Oh no')
else:
    print(result)
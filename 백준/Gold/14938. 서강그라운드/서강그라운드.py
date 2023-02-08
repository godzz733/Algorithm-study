n, m, r = map(int,input().split())
item_num = list(map(int,input().split()))
INF = int(1e9)
arr = [[INF] * (n+1) for _ in range(n+1)]
result = []
for _ in range(r):
    a, b, c = map(int, input().split())
    arr[a][b] = c
    arr[b][a] = c
for i in range(n+1):
    for j in range(n+1):
        if i==j:
            arr[i][j] = 0
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if arr[i][k] + arr[k][j] < INF:
                arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])
for i in range(1,n+1):
    num = 0
    for j in range(1,n+1):
        if arr[i][j] <= m:
            num += item_num[j-1]
    result.append(num)
print(max(result))
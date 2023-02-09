n = int(input())
INF = int(1e9)
arr = [[INF] * (n) for _ in range(n)]
result = []
name = []
while 1:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    arr[a-1][b-1] = 1
    arr[b-1][a-1] = 1
for i in range(n):
    for j in range(n):
        if i==j:
            arr[i][j] = 0

for k in range(n):
    for a in range(n):
        for b in range(n):
            arr[a][b] = min(arr[a][b], arr[a][k]+arr[k][b])
for i in range(n):
    result.append(max(arr[i]))
for i in range(n):
    if result[i] == min(result):
        name.append(i+1)
print(min(result),len(name))
print(*name)
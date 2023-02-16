n, m = map(int, input().split())
INF = int(1e9)
distance = [[INF] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    distance[a][b] = c
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
_min = INF
for i in range(1,n+1):
    _min = min(_min, distance[i][i])

print(_min) if _min<INF else print(-1)
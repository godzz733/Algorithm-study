n = int(input())
m = int(input())
INF = int(1e9)
arr = [[INF] * (n+1) for _ in range(n+1)]
visited = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a][b] = min(arr[a][b],c)

for i in range(1,n+1):
    arr[i][i] = 0
def find_path(i,j):
    if visited[i][j] == 0:
        return []
    k = visited[i][j]
    return find_path(i,k) + [k] + find_path(k,j)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]
                visited[i][j] = k

for i in range(1,n+1):
    for j in range(1,n+1):
        print(arr[i][j] if arr[i][j] != INF else 0, end=' ')
    print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if arr[i][j] in [0,INF]:
            print(0)
            continue
        path = [i] + find_path(i,j) + [j]
        print(len(path), end=' ')
        print(*path)
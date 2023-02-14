import heapq
n = int(input())
arr = [list(map(int, str(input()))) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            arr[i][j] = 0
        else:
            arr[i][j] = 1
visited = [[False] * n for _ in range(n)]
INF = int(1e9)
distance = [[INF] * n for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
distance[0][0] = 0
def dik(x,y):
    q = []
    visited[x][y] = True
    heapq.heappush(q,(0,x,y))
    while q:
        dist, x, y = heapq.heappop(q)
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            cost = distance[x][y] + arr[nx][ny]
            if distance[nx][ny] > cost:
                distance[nx][ny] = cost
                if not visited[nx][ny]:
                    heapq.heappush(q,(cost,nx,ny))
dik(0,0)
print(distance[n-1][n-1])
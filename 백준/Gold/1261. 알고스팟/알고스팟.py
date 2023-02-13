import heapq
n, m = map(int, input().split())
INF = int(1e9)
arr = [list(map(int, str(input()))) for _ in range(m)]
distance =[[INF] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dik(x,y):
    q = []
    visited[x][y] = True
    distance[x][y] = 0
    heapq.heappush(q,(0,x,y))
    while q:
        dist, x, y = heapq.heappop(q)
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue

            cost = dist + arr[nx][ny]
            if distance[nx][ny] > cost:
                distance[nx][ny] = cost
                if not visited[nx][ny]:
                    heapq.heappush(q,(cost,nx,ny))
dik(0,0)
print(distance[m-1][n-1])        
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
n, m, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]
for _ in range(k):
    a, b = map(int ,input().split())
    arr[a-1][b-1] = '#'
visited = set()
result = []
def bfs(x,y):
    cnt = 1
    q = deque()
    q.append((x,y))
    visited.add((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if (nx,ny) not in visited and arr[nx][ny] == '#':
                q.append((nx,ny))
                visited.add((nx,ny))
                cnt += 1
    result.append(cnt)
for i in range(n):
    for j in range(m):
        if (i,j) not in visited and arr[i][j] == '#':
            bfs(i,j)
print(max(result))
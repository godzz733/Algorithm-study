from collections import deque
#
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'W':
            arr[i][j] = 0
        else:
            arr[i][j] = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y,cnt):
    if not arr[x][y]:
        return 0
    _max = -1
    queue = deque([(x,y,cnt)])
    visited[x][y] = True
    while queue:
        x, y, cnt = queue.popleft()
        if _max<cnt:
            _max = cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if arr[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny,cnt+1))
    return _max
result = 0
for i in range(n):
    for j in range(m):
        visited = [[False] * m for _ in range(n)]
        result = max(result, bfs(i,j,0))
print(result)

from collections import deque
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = []
cnt = 0
def bfs(x,y):
    c = 0
    q = deque()
    q.append((x,y))
    arr[x][y] = 0
    while q:
        x, y= q.popleft()
        c += 1  
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if arr[nx][ny]:
                arr[nx][ny] = 0
                q.append((nx,ny))
    result.append(c)            
    return 1
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            if bfs(i,j):
                cnt += 1

print(cnt)
if result:
    print(max(result))
else:
    print(0)       
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == '.': arr[i][j] = 0
        elif arr[i][j] == '#': visited[i][j] = True
        elif arr[i][j] == 'v':arr[i][j] = 1
        elif arr[i][j] == 'o':arr[i][j] = 2

dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = [0,0]
def bfs(x,y):
    global visited
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    key = 0
    a = b = 0
    if arr[x][y] == 1: a += 1
    elif arr[x][y] == 2: b += 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or nx >= n or ny <0 or ny >= m:
                key = 1
                continue
            if visited[nx][ny]: continue
            visited[nx][ny] = True
            if arr[nx][ny] == 1:
                a += 1
                q.append((nx,ny))
            elif arr[nx][ny] == 2:
                b += 1
                q.append((nx,ny))
            else:
                q.append((nx,ny))
    if not key:
        if a >= b: b = 0
        else: a = 0
        return [a,b]
    return [0,0]
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            tem = bfs(i,j)
            ans[0] += tem[0]
            ans[1] += tem[1]
print(*ans[::-1])
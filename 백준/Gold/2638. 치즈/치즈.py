import sys
from collections import deque
sys.setrecursionlimit(10001)
n, m = map(int, input().split())
arr= [list(map(int ,input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
erase = set()
def dfs(x,y):
    if visited[x][y]:
        return 0
    global erase
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if arr[nx][ny]:
            erase.add((x,y))
            visited[nx][ny] = True
        elif not arr[nx][ny] and not visited[nx][ny]:
            dfs(nx,ny)
def bfs():
    num = 0
    for i in range(n):
        for j in range(m):
            cnt = 0
            if arr[i][j]:
                num += 1
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if (nx,ny) in erase:
                        cnt += 1
                if cnt >= 2:
                    arr[i][j] = 0
    if num:
        return 1
    else:
        return 0

result = 0
while 1:
    visited = [[False] * m for _ in range(n)]
    dfs(0,0)
    a = bfs()
    result += a
    if not a:
        break
print(result)
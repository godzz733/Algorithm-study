import sys;input = sys.stdin.readline
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(n):
    visited = [[int(1e9)] * n for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = arr[0][0]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n: continue
            if visited[nx][ny] > visited[x][y] + arr[nx][ny]:
                visited[nx][ny] = visited[x][y] + arr[nx][ny]
                q.append((nx,ny))
    return visited[n-1][n-1]
idx = 1
while 1:
    n = int(input())
    if not n: break
    arr = [list(map(int, input().split())) for _ in range(n)]
    print("Problem {}: {}".format(idx, bfs(n)))
    idx += 1
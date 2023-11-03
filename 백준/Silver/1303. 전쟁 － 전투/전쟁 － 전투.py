import sys;input = sys.stdin.readline
from collections import deque
m,n = map(int,input().split())
arr = list(input() for _ in range(n))
ans = [0,0]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
vi = [[0]*m for _ in range(n)]
def bfs(x,y):
    q = deque()
    q.append([x,y])
    ori = arr[x][y]
    vi[x][y] = 1
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and not vi[nx][ny] and arr[nx][ny] == ori:
                vi[nx][ny] = 1
                cnt += 1
                q.append([nx,ny])
    return cnt
for i in range(n):
    for j in range(m):
        if not vi[i][j]:
            tem = bfs(i,j)
            if arr[i][j] == 'W':
                ans[0] += tem**2
            else:
                ans[1] += tem**2
print(*ans)
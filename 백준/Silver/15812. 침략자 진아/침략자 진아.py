import sys; input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
arr = list(list(map(int,input().rstrip())) for _ in range(n))

ans = 999999
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def solve(x,y,house):
    global ans
    q = deque()
    q.append((x[0],x[1]))
    q.append((y[0],y[1]))
    cnt = 0
    lst = [[0]*m for _ in range(n)]
    lst[x[0]][x[1]] = 1
    lst[y[0]][y[1]] = 1
    while house:
        if cnt >= ans:
            return 9999
        tem = []
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and lst[nx][ny] == 0:
                    if arr[nx][ny] == 1:
                        house -= 1
                    lst[nx][ny] = 1
                    tem.append((nx,ny))
        cnt += 1
        q.extend(tem)
    return cnt

t = []
num = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            t.append((i,j))
        else:
            num += 1

for i in range(len(t)-1):
    for j in range(i+1,len(t)):
        ans = min(ans,solve(t[i],t[j],num))
print(ans)
from collections import deque
n,m,k = map(int,input().split())
arr = [list(input()) for _ in range(n)]
ans = [[[0] * m for _ in range(n)] for _ in range(k)]
q = deque()
tem = set()
tem.add((n-1,0))
q.append((n-1,0,0,tem.copy()))
ans[0][0][0] = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def inRange(x,y):
    if x<0 or x>=n or y<0 or y>=m or arr[x][y] == 'T':
        return False
    return True
while q:
    x,y,cnt,_set = q.popleft()
    for i in range(4):
        tem = _set.copy()
        nx = x + dx[i]
        ny = y + dy[i]
        if not inRange(nx,ny) or (nx,ny) in tem or cnt == k-1: continue
        tem.add((nx,ny))
        ans[cnt+1][nx][ny] += 1
        q.append((nx,ny,cnt+1,tem))

print(ans[k-1][0][m-1])
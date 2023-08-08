from collections import deque
n,m,k = map(int,input().split())
arr = [list(input()) for _ in range(n)]
ans = 0
q = deque()
tem = set()
tem.add((n-1,0))
q.append((n-1,0,0,tem.copy()))
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
        if not inRange(nx,ny) or (nx,ny) in tem: continue
        if cnt == k-2 and nx == 0 and ny == m-1: ans += 1
        tem.add((nx,ny))
        q.append((nx,ny,cnt+1,tem))

print(ans)
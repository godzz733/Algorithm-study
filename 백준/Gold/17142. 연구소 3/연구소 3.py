import sys; input = sys.stdin.readline
from itertools import combinations
from collections import deque
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
lst = [[0] * n for _ in range(n)]
v = []
num = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            v.append((i,j))
            lst[i][j] = 3
        elif arr[i][j] == 0:
            num += 1
        else:
            lst[i][j] = 1
ans = 2600 if num else 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def solve(v):
    q = deque()
    cnt = num
    virus = [lst[i][::] for i in range(n)]
    for x,y in v:
        virus[x][y] = 2
        q.append([x,y,0])
    while q:
        x,y,t = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and virus[nx][ny] != 1 and virus[nx][ny] != 2:
                if virus[nx][ny] == 0:
                    cnt -= 1
                virus[nx][ny] = 2
                q.append([nx,ny,t+1])
                if cnt == 0:
                    return t + 1 
    return 2600

for i in combinations(v,m):
    if ans <= 1:
        break
    ans = min(ans,solve(list(i)))

print(ans if ans != 2600 else -1)


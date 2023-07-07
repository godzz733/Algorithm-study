from collections import deque
n, m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == "I":
            arr[i][j] = -1
            a,b = i,j
            break
q = deque()
q.append((a,b))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = 0
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y +dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m or arr[nx][ny] == -1 or arr[nx][ny] == 'X': continue
        if arr[nx][ny] == 'P': ans += 1
        arr[nx][ny] = -1
        q.append((nx,ny))
print(ans) if ans else print('TT')
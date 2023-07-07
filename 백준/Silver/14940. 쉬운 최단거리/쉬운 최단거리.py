from collections import deque
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
a = b = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            a = i
            b = j
            break
q = deque()
q.append([a,b])
dx = [1,-1,0,0]
dy = [0,0,1,-1]
arr[a][b] = 0
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx >=n or ny<0 or ny>=m or not arr[nx][ny]: continue
        if arr[nx][ny] == 1:
            arr[nx][ny] = arr[x][y] + 1
            q.append([nx,ny])
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = -1
for i in range(4):
    nx = a + dx[i]
    ny = b + dy[i]
    if nx<0 or nx >=n or ny<0 or ny>=m or not arr[nx][ny]: continue
    arr[nx][ny] = 1
for i in range(n):
    for j in range(m-1):
        print(arr[i][j], end=" ")
    print(arr[i][j+1])
        
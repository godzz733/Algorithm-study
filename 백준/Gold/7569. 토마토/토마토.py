from collections import deque

n, m, h = map(int,input().split())
arr = []
for _ in range(h):
    arr.append([list(map(int, input().split())) for _ in range(m)])

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
li = []
for z in range(h):
    for x in range(m):
        for y in range(n):
            if arr[z][x][y] == 1:
                li.append((z,x,y))

def bfs():
    global cnt
    queue = deque()
    cnt = 0
    while li:
        queue.extend(li)
        li.clear()
        while queue:
            z,x,y = queue.popleft()
            for i in range(6):
                nx = dx[i] + x
                ny = dy[i] + y
                nz = dz[i] + z
                if nx<0 or nx>=m or ny<0 or ny>=n or nz<0 or nz>=h:
                    continue
                if arr[nz][nx][ny] == 0:
                    arr[nz][nx][ny] = 1
                    li.append((nz,nx,ny))
        cnt += 1

bfs()

key = 0
for z in range(h):
    for x in range(m):
        for y in range(n):
            if arr[z][x][y] == 0:
                key += 1

if key>0:
    print(-1)
else:
    if cnt-1 == -1:
        print(0)
    else:
        print(cnt-1)
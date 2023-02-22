from collections import deque
dx = [-1,0,0,1]
dy = [0,-1,1,0]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0
def bfs(x,y,cnt):
    global result
    q = deque()
    q.append((x,y,cnt))
    baby = 2
    feed = 0
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    lst = []
    arr[x][y] = 0

    while 1:
        stop = 0
        while q:
            x, y, cnt = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y +dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue
                if not visited[nx][ny]:
                    if 0<arr[nx][ny]<baby:
                        visited[nx][ny] = True
                        if not lst:
                            lst.append((nx,ny,cnt+1))
                        else:
                            if cnt+1 <= lst[0][2]:
                                lst.append((nx,ny,cnt+1))
                    elif arr[nx][ny]<=baby:
                        visited[nx][ny] = True
                        q.append((nx,ny,cnt+1))
        if lst:
            lst.sort(key=lambda x:(x[0],x[1]))
            x, y, cnt = lst[0][0], lst[0][1], lst[0][2]
            arr[x][y] = 0
            result += cnt
            stop += 1
            feed += 1
            lst.clear()
            q.append((x,y,0))
            visited = [[False] * n for _ in range(n)]
        if feed == baby:
            baby += 1
            feed = 0
        if not stop:
            return
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            bfs(i,j, 0)
print(result)
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y,cnt):
    q = deque()
    q.append((x,y))
    block.add((x,y))
    visited[x][y] = True
    cnt += 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if not visited[nx][ny] and not arr[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
                cnt += 1
                block.add((nx,ny))
    return cnt

n, m = map(int,input().split())
arr= [list(map(int,input())) for _ in range(n)]
visited= [[False] * m for _ in range(n)]
move = [[(0,0)]*m for _ in range(n)]
idx = 1
for i in range(n):
    for j in range(m):
        if not arr[i][j] and not visited[i][j]:
            block = set()
            cnt = bfs(i,j,0)
            for x, y in block:
                move[x][y] = (cnt,idx)
            idx += 1
result = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            cnt = 1
            a = set()
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                if move[nx][ny][1] not in a:
                    a.add(move[nx][ny][1])
                    cnt += move[nx][ny][0]
            result[i][j] = cnt%10
for i in range(n):
    print(''.join(map(str,result[i])))
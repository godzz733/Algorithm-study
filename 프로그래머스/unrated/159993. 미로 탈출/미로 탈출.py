from collections import deque
arr = []
dx = [-1,1,0,0]
dy = [0,0,1,-1]
visited = []
def solution(maps):
    global arr, visited
    arr = [[0] * len(maps[0]) for _ in range(len(maps))]
    visited = [[[False] * len(maps[0]) for _ in range(len(maps))] for _ in range(2)]
    start = [0,0]
    # -1 벽 1 탈출 2 레버
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "X":
                arr[i][j] = -1
            elif maps[i][j] == "E":
                arr[i][j] = 1
            elif maps[i][j] == "L":
                arr[i][j] = 2
            elif maps[i][j] == "S":
                arr[i][j] = 0
                start = [i,j]
    answer = bfs(start[0],start[1],len(maps), len(maps[0]))
    return answer
def bfs(x,y,n,m):
    q = deque()
    q2 = deque()
    q.append((x,y,0))
    visited[0][x][y] = True
    key = 0
    ans = -1
    while q:
        if key:
            break
        x,y,cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m or visited[0][nx][ny] or arr[nx][ny] == -1:
                continue
            if arr[nx][ny] != 2:
                visited[0][nx][ny] = True
                q.append((nx,ny,cnt+1))
            else:
                visited[1][nx][ny] = True
                q2.append((nx,ny,cnt+1))
                key = 1
                break
    while q2:
        x,y,cnt = q2.popleft()
        print(x,y,cnt)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m or visited[1][nx][ny] or arr[nx][ny] == -1:
                continue
            if arr[nx][ny] != 1:
                visited[1][nx][ny] = True
                q2.append((nx,ny,cnt+1))
            else:
                return cnt+1
    return ans
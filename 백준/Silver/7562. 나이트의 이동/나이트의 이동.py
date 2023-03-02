from collections import deque
t = int(input())
dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,2,1,-1,-2]
def bfs(x,y):
    q = deque()
    q.append((x, y, 0))
    visited = set()
    visited.add((x, y))
    while q:
        x, y, cnt = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if nx == st and ny == en:
                return cnt + 1
            if (nx, ny) not in visited:
                q.append((nx, ny, cnt + 1))
                visited.add((nx, ny))
for _ in range(t):
    n = int(input())
    x,y = map(int,input().split())
    st,en = map(int, input().split())
    if x==st and y==en:
        print(0)
    else:
        print(bfs(x,y))
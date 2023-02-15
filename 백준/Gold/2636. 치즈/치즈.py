from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not arr[nx][ny] and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
            else:
                visited[nx][ny] = True
                arr[nx][ny] = 0
num = 0
result = []
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            num += 1
result.append(num)
num = 1

while num > 0:
    num = 0
    visited = [[False] * m for _ in range(n)]
    bfs(0, 0)
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                num += 1
    result.append(num)

if result:
    print(len(result)-1)
    print(result[-2])

else:
    print(0)
    print(0)


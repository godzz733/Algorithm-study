from collections import deque
import copy
#
n, m = map(int, input().split())
li = [list(input()) for _ in range(n)]
result = []
for i in range(n):
    for j in range(m):
        if li[i][j] == 'W':
            li[i][j] = 0
        else:
            li[i][j] = 1
visited = [[False] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    global arr
    arr = copy.deepcopy(li)
    visited = [[False] * m for _ in range(n)]
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not visited[nx][ny] and arr[nx][ny]:
                arr[nx][ny] += arr[x][y]
                queue.append((nx, ny))
                visited[nx][ny] = True
for i in range(n):
    _min = 0
    for j in range(m):
        bfs(i,j)
        for k in range(n):
            result.append(max(arr[k]))
print(max(result)-1)


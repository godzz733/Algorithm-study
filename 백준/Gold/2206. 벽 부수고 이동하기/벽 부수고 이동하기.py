from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, str(input()))) for _ in range(n)]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]


def bfs():
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        x, y, z = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
            elif arr[nx][ny] == 1 and z == 0:
                visited[nx][ny][z + 1] = visited[x][y][z] + 1
                queue.append((nx, ny, z + 1))
    return -1


print(bfs())

from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, str(input()))) for _ in range(n)]

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]  # 특정 위치와 벽을 부쉈을 경우, 안부쉈을경우를 나타내기위해 3차원 리스트로 초기화


# visited의 [x]는 행 [y]는 열 [z][0]은 벽을 안부순경우, [z][1] 부순경우 이다

def bfs():
    queue = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        x, y, z = queue.popleft()
        if x == n - 1 and y == m - 1:  # 목표 지점에 도달할 경우 리턴, 일단 먼저 도착하는게 최단경로이므로 이래도 됨
            return visited[x][y][z]
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 0 and visited[nx][ny][z] == 0:  # 만약 벽이 없고 방문 하지 않았다면
                visited[nx][ny][z] = visited[x][y][z] + 1  # 거리를 기존 위치에서 1 늘려서 저장
                queue.append((nx, ny, z))  # 다음 위치를 큐에 넣음
            elif arr[nx][ny] == 1 and z == 0:  # 만약 벽이고 지금까지 벽을 부순적이 없다면
                visited[nx][ny][z + 1] = visited[x][y][z] + 1  # 벽을 부순 경우의 값을 현재 위치 +1로 저장
                queue.append((nx, ny, z + 1))  # 벽을 부순 경우를 큐에 넣음
    return -1


print(bfs())

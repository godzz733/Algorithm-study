from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
x, y, d = map(int, input().split())
en_x, en_y, en_d = map(int, input().split())
dx = [0, 0, 0, 1, -1]  # 동서남북
dy = [0, 1, -1, 0, 0]
visited = set()
q = deque()
q.append((x - 1, y - 1, d, 0))  # x,y,방향,명령횟수
visited.add((x - 1, y - 1, d))
key = 0
while q:
    x, y, direction, cnt = q.popleft()
    if x == (en_x - 1) and y == (en_y - 1) and direction == en_d:
        result = cnt
        key += 1
    if key:
        break
    if direction == 1:
        if (x,y,3) not in visited:
            q.append((x, y, 3, cnt+1))
            visited.add((x, y, 3))
        if (x,y,4) not in visited:
            q.append((x, y, 4, cnt+1))
            visited.add((x, y, 4))
    elif direction == 2:
        if (x, y, 3) not in visited:
            q.append((x, y, 3, cnt + 1))
            visited.add((x, y, 3))
        if (x, y, 4) not in visited:
            q.append((x, y, 4, cnt + 1))
            visited.add((x, y, 4))
    elif direction == 3:
        if (x, y, 1) not in visited:
            q.append((x, y, 1, cnt + 1))
            visited.add((x, y, 1))
        if (x, y, 2) not in visited:
            q.append((x, y, 2, cnt + 1))
            visited.add((x, y, 2))
    elif direction == 4:
        if (x, y, 1) not in visited:
            q.append((x, y, 1, cnt + 1))
            visited.add((x, y, 1))
        if (x, y, 2) not in visited:
            q.append((x, y, 2, cnt + 1))
            visited.add((x, y, 2))

    for i in range(1, 4):
        nx = x + dx[direction] * i
        ny = y + dy[direction] * i
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            break
        elif arr[nx][ny]:
            break
        if not arr[nx][ny] and (nx, ny, direction) not in visited:
            visited.add((nx, ny, direction))
            q.append((nx, ny, direction, cnt + 1))
print(result)

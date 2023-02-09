from collections import deque
import sys
t = int(input())
def fire(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if arr[nx][ny] == '.' or arr[nx][ny] == '@':
            arr[nx][ny] = '*'
            fi.append((nx, ny))

def bfs(x, y, cnt):
    queue = deque([])
    li = [(x, y, cnt)]
    while li:
        queue.extend(li)
        li.clear()
        for i in range(len(fi)):
            a, b = fi.popleft()
            fire(a, b)
        while queue:
            x, y, cnt = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    return cnt
                if arr[nx][ny] == '#' or arr[nx][ny] == '*':
                    continue
                if arr[nx][ny] == '.':
                    arr[nx][ny] = '@'
                    arr[x][y] = '0'
                    li.append((nx, ny, cnt + 1))
for _ in range(t):
    n, m = map(int, input().split())
    arr = [list(sys.stdin.readline()) for _ in range(m)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    fire_arr = []
    for i in range(m):
        for j in range(n):
            if arr[i][j] == '*':
                fire_arr.append((i, j))
    fi = deque(fire_arr)

    for i in range(m):
        for j in range(n):
            if arr[i][j] == '@':
                st_x, st_y = i, j
    result = bfs(st_x, st_y, 1)

    print(result) if result else print('IMPOSSIBLE')

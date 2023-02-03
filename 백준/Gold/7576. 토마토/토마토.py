import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(m):
    arr.append([*map(int, sys.stdin.readline().rstrip().split())])
tomato = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            tomato.append((i, j))

cnt = 0


def bfs():
    global cnt
    queue = deque()
    while tomato:
        queue.extend(tomato)
        tomato.clear()
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    pass
                else:
                    if arr[nx][ny] == 0:
                        arr[nx][ny] = 1
                        tomato.append((nx, ny))
        cnt += 1
    return cnt
key = 0
bfs()
for i in arr:
    for j in range(n):
        if i[j] == 0:
            key = 1
if key == 0:
    print(cnt-1) # 토마토가 다 익은뒤에도 마지막으로 한번 더 연산하므로 1을 빼줌
else:
    print(-1)

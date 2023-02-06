from collections import deque
import copy

n, a, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0
visited = [[False] * n for _ in range(n)]
def door(x,y):
    if visited[x][y] == True:
        return
    visited[x][y] = True
    country = []
    population = []
    country.append((x,y))
    population.append(arr[x][y])
    queue = deque([(x,y)])
    while queue:
        q = queue.popleft()
        x = q[0]
        y = q[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if not visited[nx][ny]:
                if a<=abs(arr[nx][ny]-arr[x][y])<=b:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    country.append((nx,ny))
                    population.append(arr[nx][ny])
    for i in country:
        arr[i[0]][i[1]] = sum(population)//len(population)
while 1:
    cnt += 1
    test = copy.deepcopy(arr)
    for i in range(n):
        for j in range(n):
            door(i,j)
    visited = [[False] * n for _ in range(n)]
    if arr == test:
        break
print(cnt-1)
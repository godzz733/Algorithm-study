from collections import deque
# 모든 육지를 순회하면서 육지를 라벨링 -> 다시 모든 육지를 순회하면서 가장 짧은 다리를 건설
n = int(input())
arr = [list(map(int ,input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

num = []
land = set()
def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited = set()
    water = set()
    visited.add((x,y))
    water_visited = set()
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if (nx,ny) not in visited:
                if arr[nx][ny]:
                    visited.add((nx,ny))
                    q.append((nx,ny))
                    land.add((nx,ny))
                elif not arr[nx][ny]:
                    water.add((x,y,0)) # 물과의 경계를 저장, x,y,라벨,이동횟수
    q.extend(water)
    while q:
        x, y, result = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not arr[nx][ny] and (nx,ny) not in water_visited:
                q.append((nx, ny,result + 1))
                water_visited.add((nx,ny))
            elif arr[nx][ny] and (nx,ny) not in visited:
                num.append(result)
                return
for i in range(n):
    for j in range(n):
        if (i,j) not in land and arr[i][j]:
            bfs(i,j)
print(min(num))
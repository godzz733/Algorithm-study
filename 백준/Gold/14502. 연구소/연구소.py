import copy
from collections import deque
import itertools
n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = 0
can = []
arr = copy.deepcopy(lst)
def virus():
    cnt = 0
    virus = deque()
    visited = set()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                virus.append((i,j))
                visited.add((i,j))
    while virus:
        x, y = virus.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m or arr[nx][ny] != 0:
                continue
            if (nx,ny) not in visited:
                arr[nx][ny] = 2
                visited.add((nx,ny))
                virus.append((nx,ny))
    for i in range(n):
        for j in range(m):
            if not arr[i][j]:
                cnt += 1
    return cnt


for i in range(n):
    for j in range(m):
        if not arr[i][j]:
            can.append((i,j))

test = list(itertools.combinations(can,3))
for i in test:
    arr = copy.deepcopy(lst)
    for j in i:
        arr[j[0]][j[1]] = 1
    result = max(result,virus())

print(result)
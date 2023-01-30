import sys
from collections import deque
input = sys.stdin.readline
a,b = map(int,input().rstrip().split())
arr = []
for i in range(a):
    li = str(input().rstrip())
    arr.append(list(map(int,li)))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=a or ny<0 or ny>=b:
                continue
            if arr[nx][ny] ==0:
                continue
            if arr[nx][ny]==1:
                arr[nx][ny] = arr[x][y] + 1
                queue.append((nx,ny))
    return arr[a-1][b-1]
print(dfs(0,0))
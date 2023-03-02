# 반드시 가장 높은 봉우리에서 시작
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y,k):
    global result
    q = deque()
    q.append((x,y,k,1,arr[x][y],[(x,y)]))
    while q:
        x, y, l, road, now, visited = q.popleft()
        if road > result:
            result = road
        for i in range(4):
            post_visited = visited[:]
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if arr[nx][ny] < now and (nx,ny) not in visited:
                post_visited.append((nx,ny))
                q.append((nx,ny,l,road+1,arr[nx][ny],post_visited))
            elif arr[nx][ny] >= now and l>0 and (nx,ny) not in visited:
                if arr[nx][ny] -l < now and now-1 >= 0:
                    post_visited.append((nx,ny))
                    q.append((nx,ny,0,road+1,now-1,post_visited))

t = int(input())
for tc in range(1,t+1):
    n, z = map(int, input().split())
    arr = []
    high = 0
    high_set = set()
    result = 0
    for _ in range(n):
        lst = [*map(int,input().split())]
        if high < max(lst):
            high = max(lst)
        arr.append(lst)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == high:
                high_set.add((i,j))
    for x,y in high_set:
        bfs(x,y,z)
    print(f'#{tc} {result}')
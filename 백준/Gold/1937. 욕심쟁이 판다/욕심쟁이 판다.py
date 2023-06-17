from collections import deque
dx = [-1,1,0,0]
dy = [0,0,1,-1]
def bfs(x,y):
    global visited, ans
    q = deque()
    q.append((x,y,1))
    ori = (x,y)
    max_ans = 1
    while q:
        x,y,cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n: continue
            if not visited[nx][ny] and arr[nx][ny] > arr[x][y]:
                q.append((nx,ny,cnt+1))
                max_ans = max(max_ans,cnt+1)
            elif visited[nx][ny] and arr[nx][ny] > arr[x][y]:
                max_ans = max(max_ans,cnt+visited[nx][ny])
    visited[ori[0]][ori[1]] = max_ans
    ans = max(max_ans,ans)

n = int(input())
arr = [[*map(int, input().split())] for _ in range(n)]
visited = [[0] * n for _ in range(n)]
ans = 0
a = []
for i in range(n):
    for j in range(n):
        a.append((arr[i][j],i,j))
a.sort(reverse=True)
for x,i,j in a:
    bfs(i,j)
print(ans)
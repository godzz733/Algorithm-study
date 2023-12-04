import sys; input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(input() for _ in range(n))
dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = 0
visited = [False] * 26
visited[ord(arr[0][0])-65] = True
def dfs(x,y,cnt):
    global ans
    ans = max(ans,cnt)
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and visited[ord(arr[nx][ny])-65] == False:
            visited[ord(arr[nx][ny])-65] = True
            dfs(nx,ny,cnt+1)
            visited[ord(arr[nx][ny])-65] = False
dfs(0,0,1)
print(ans)
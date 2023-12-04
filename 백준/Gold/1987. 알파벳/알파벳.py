import sys; input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(input() for _ in range(n))
D = ((1, 0), (0, 1), (-1, 0), (0, -1))
ans = 0
visited = [[0] * m for _ in range(n)]
stack = [(0,0,1,1<<(ord(arr[0][0])-65))]
while stack:
    x,y,cnt,check = stack.pop()
    ans = max(ans,cnt)
    if ans == 26:
        print(26)
        exit()
    for i in range(4):
        nx,ny = x+D[i][0],y+D[i][1]
        if 0<=nx<n and 0<=ny<m and not check & (1<<(ord(arr[nx][ny])-65)):
            tem = check | (1<<(ord(arr[nx][ny])-65))
            if tem != visited[nx][ny]:
                visited[nx][ny] = tem
                stack.append((nx,ny,cnt+1,tem))
print(ans)
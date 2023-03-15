import heapq as heq
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
m,x,y = map(int,input().split())
vi = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            vi.append([arr[i][j],i,j])
def bfs():
    for _ in range(m):
        q = []
        for cnt,x,y in vi:
            heq.heappush(q,(cnt,x,y))
        vi.clear()
        while q:
            cnt, x, y = heq.heappop(q)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue
                if not arr[nx][ny]:
                    arr[nx][ny] = cnt
                    vi.append((cnt,nx,ny))
bfs()
print(arr[x-1][y-1])
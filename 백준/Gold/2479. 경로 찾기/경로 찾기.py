from collections import deque
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
lst = [list(str(input())) for _ in range(n)]
visited = [False] * (n+1)
for i in range(n-1):
    for k in range(i+1,n):
        cnt = 0
        for j in range(m):
            if lst[i][j] == lst[k][j]:
                cnt += 1
        if m-cnt == 1:
            arr[i+1].append(k+1)
            arr[k+1].append(i+1)
a, b = map(int,input().split())
def bfs(x):
    q = deque()
    q.append((x,[x]))
    while q:
        x, result = q.popleft()
        visited[x] = True
        if not result:
            continue
        for i in arr[x]:
            if i == b:
                return result + [i]
            if not visited[i]:
                q.append((i,result+[i]))
result = bfs(a)
if not result:
    print(-1)
else:
    print(*result)
from collections import deque
a,b = map(int, input().split())
n,m = map(int, input().split())
visited = [False] * (n+1)
arr = [[] for _ in range(n+1)]
for _ in range(m):
    u, v  = map(int,input().split())
    arr[u].append(v)
    arr[v].append(u)

def bfs(c,v):
    q = deque()
    q.append((c,v))
    visited[c] = True 
    while q:
        x,y = q.popleft()
              
        if x == b:
            return y
        for i in arr[x]:
            if not visited[i]:
                visited[i] = True
                q.append((i,y+1))
    return 0

result = bfs(a,0)
if a==b:
    print(0)
elif not result:
    print(-1)
else:
    print(result)

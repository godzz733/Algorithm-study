n,m = map(int,input().split())
parent = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    parent[a].append(b)
    parent[b].append(a)
visited = [0]*n
ans = 0
def back(cnt,x):
    global ans
    if cnt==5:
        ans = 1
        return
    for i in parent[x]:
        if not visited[i]:
            visited[i] = 1
            back(cnt+1,i)
            visited[i] = 0
for i in range(n):
    visited[i] = 1
    back(1,i)
    visited[i] = 0
print(ans)
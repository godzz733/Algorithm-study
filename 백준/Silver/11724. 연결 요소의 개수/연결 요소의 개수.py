import sys
input = sys.stdin.readline
n,m = map(int,input().rstrip().split())
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0
for _ in range(m):
    a, b = map(int,input().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(v,arr,visited):
    if visited[v]==True:
        return False
    visited[v] = True
    for i in arr[v]:
        if not visited[i]:
            dfs(i,arr,visited)
    return True



for i in range(1,n+1):
    if dfs(i,arr,visited)==True:
        count +=1
print(count)

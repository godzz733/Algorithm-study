import sys
from collections import deque
input = sys.stdin.readline
n,m,start = map(int,input().split())
visited = [False] * (n+1)
arr = [[] for _ in range(n+1)]
graph = [[]]
for i in range(m):
    a,b = list(map(int,input().split()))
    arr[a].append(b)
    arr[b].append(a) 
for i in range(1,n+1):
    graph.append(sorted(arr[i]))
    

def dfs(graph, visited, start):
    visited[start] = True
    print(f'{start}', end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,visited,i)
dfs(graph,visited,start)
print('',end='\n')
visited = [False] * (n+1)
def bfs(graph, visited, start):
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        print(f'{v}',end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
bfs(graph,visited,start)


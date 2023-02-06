from collections import deque
import sys
sys.setrecursionlimit(100000)

n, m, start = map(int, input().split())
node = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i] = sorted(graph[i], reverse=True)


def dfs(graph, visited, start):
    global cnt
    cnt += 1
    visited[start] = True
    node[start] = cnt
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, visited, i)


dfs(graph, visited, start)

for i in range(1,n+1):
    print(node[i])
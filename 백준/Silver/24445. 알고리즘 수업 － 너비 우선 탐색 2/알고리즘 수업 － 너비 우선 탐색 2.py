from collections import deque

n, m, start = map(int, input().split())
node = [0] * (n+1)
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n + 1):
    graph[i] = sorted(graph[i], reverse=True)


def bfs():
    cnt = 0
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        cnt += 1
        node[v] = cnt
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

bfs()
for i in range(1,n+1):
    print(node[i])
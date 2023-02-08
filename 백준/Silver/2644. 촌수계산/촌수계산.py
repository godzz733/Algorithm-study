from collections import deque

n = int(input())
a, b = map(int, input().split())
visited = [False] * (n + 1)
m = int(input())
arr = [[] for _ in range(n + 1)]
cnt = 0
result = 0
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

def bfs(a):
    global cnt, result
    queue = deque()
    li = [a]
    while li:
        cnt += 1
        queue.extend(li)
        li.clear()
        while queue:
            v = queue.popleft()
            if not visited[v]:
                visited[v] = True
                for i in arr[v]:
                    if i == b:
                        result = cnt
                        li.clear()
                        break
                    li.append(i)


if a == b:
    print(0)
else:
    bfs(a)
    if not result:
        print(-1)
    else:
        print(result)

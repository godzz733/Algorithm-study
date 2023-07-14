from collections import deque
n = int(input())
parent = [0] * (n + 1)
parent[1] = 1
q = deque()
arr = [[] for _ in range(n + 1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    if parent[a]:
        parent[b] = a
        q.append(b)
    elif parent[b]:
        parent[a] = b
        q.append(a)
    else:
        arr[a].append(b)
        arr[b].append(a)
while q:
    now = q.popleft()
    for x in arr[now]:
        if not parent[x]:
            parent[x] = now
            q.append(x)


for i in range(2, n + 1):
    print(parent[i])
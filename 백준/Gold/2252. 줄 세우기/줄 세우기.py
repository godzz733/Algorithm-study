from collections import deque
v,e = map(int,input().split())
arr = [[] for _ in range(v+1)]
indegrees = [0] * (v+1)
for _ in range(e):
    a, b = map(int,input().split())
    indegrees[b] += 1
    arr[a].append(b)
q = deque()

for i in range(1,v+1):
    if not indegrees[i]:
        q.append(i)
result = []
while q:
    x = q.popleft()
    result.append(x)
    for i in arr[x]:
        indegrees[i] -= 1
        if indegrees[i] == 0:
            q.append(i)

print(*result)
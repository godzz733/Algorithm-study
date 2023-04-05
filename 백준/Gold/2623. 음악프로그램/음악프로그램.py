from collections import deque
n, m = map(int,input().split())
indegrees = [0] * (n+1)
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, *lst = map(int,input().split())
    for i in range(len(lst)-1):
        indegrees[lst[i+1]] += 1
        arr[lst[i]].append(lst[i+1])
result = []
q = deque()
for i in range(1,n+1):
    if not indegrees[i]:
        q.append(i)

while q:
    x = q.popleft()
    result.append(x)
    for i in arr[x]:
        indegrees[i] -= 1
        if indegrees[i] == 0:
            q.append(i)
if len(result) != n:
    print(0)
else:
    for i in result:
        print(i)
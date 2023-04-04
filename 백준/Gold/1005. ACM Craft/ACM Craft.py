from collections import deque
for _ in range(int(input())):
    n,k = map(int,input().split())
    arr = [0] + list(map(int,input().split()))
    indegree = [0] * (n+1)
    dp = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(k):
        a, b = map(int,input().split())
        graph[a].append(b)
        indegree[b] += 1
    w = int(input())
    q = deque()
    for i in range(1,n+1):
        if not indegree[i]:
            q.append((i,arr[i]))
    while q:
        x, t = q.popleft()

        if x == w:
            print(t)
            break
        for i in graph[x]:
            indegree[i] -= 1
            dp[i] = max(t+arr[i],dp[i])
            if indegree[i] == 0:
                q.append((i,dp[i]))
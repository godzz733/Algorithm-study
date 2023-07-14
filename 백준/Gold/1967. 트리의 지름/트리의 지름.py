from collections import deque
n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    arr[a].append((b,c))
출력 = 0
for j in range(1,n+1):
    q = deque()
    result = []
    visited = [False] * (n+1)
    visited[1] = True
    for i in arr[j]:
        q.append((i[0],i[1]))
        visited[i[0]] = True
        ans = 0
        while q:
            now,cnt = q.popleft()
            ans = max(ans,cnt)
            for nxt, cost in arr[now]:
                if cnt + cost < ans: continue
                if not visited[nxt]:
                    q.append((nxt,cnt+cost))
                    visited[nxt] = True
        result.append(ans)
    if len(result) == 0:
        break
    elif len(result) == 1:
        출력 = max(출력,result[0])
    else:
        result.sort()
        출력 = max(출력,result[-1] + result[-2])
print(출력)
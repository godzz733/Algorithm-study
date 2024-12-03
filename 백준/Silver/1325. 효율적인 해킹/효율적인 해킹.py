import sys; input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
arr = [set() for _ in range(n+1)]
cycle = [0] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    arr[b].add(a)
    if b in arr[a]:
        cycle[b] = a
        cycle[a] = b
ans = [0] * (n+1)

for i in range(1,n+1):
    if cycle[i] and ans[cycle[i]]:
        ans[i] = ans[cycle[i]]
    else:
        v = [0] * (n+1)
        v[i] = 1
        q = deque([i])
        t = 1
        while q:
            x = q.popleft()
            for nx in arr[x]:
                if not v[nx]:
                    v[nx] = 1
                    q.append(nx)
                    t += 1
        ans[i] = t
_max = max(ans)
print(*[i for i in range(1,n+1) if ans[i] == _max])
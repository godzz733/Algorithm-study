import sys; input = sys.stdin.readline
import heapq as h
n,m = map(int,input().split())
arr = [[] for _ in range(n)]
for i in range(n):
    t = list(input().rstrip())
    for j in range(n):
        if i != j:
            arr[i].append((int(t[j]),j,0))
            arr[i].append((int(t[j])/2,j,1))

q = []
h.heappush(q,(0,0,0))
d = [[0] + [int(1e9)]*(n-1) for _ in range(m+1)]

while q:
    cost, now, cnt = h.heappop(q)
    if d[cnt][now] < cost:
        continue
    for i in arr[now]:
        dist = cost + i[0]
        if cnt + i[2] <= m and dist < d[cnt+i[2]][i[1]]:
            d[cnt+i[2]][i[1]] = dist
            h.heappush(q,(dist,i[1],cnt+i[2]))
ans = int(1e9)
for i in range(m+1):
    ans = min(ans,d[i][1])
print(ans)
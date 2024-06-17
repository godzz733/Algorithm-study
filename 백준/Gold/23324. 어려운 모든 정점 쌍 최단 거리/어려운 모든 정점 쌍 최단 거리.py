import sys; input = sys.stdin.readline
import heapq as h
n,m,k = map(int,input().split())
q = []
arr = [[] for _ in range(n+1)]
d = [1e9]*(n+1)
st = 0
for i in range(m):
    a,b = map(int,input().split())
    if i == k-1:
        st = a
        arr[a].append((b,1))
        arr[b].append((a,1))
    else:
        arr[a].append((b,0))
        arr[b].append((a,0))
d[st] = 0
d[0] = 0
h.heappush(q,(0,st))
while q:
    dist,now = h.heappop(q)
    if d[now] < dist:
        continue
    for i in arr[now]:
        cost = dist + i[1]
        if cost < d[i[0]]:
            d[i[0]] = cost
            h.heappush(q,(cost,i[0]))
cnt = sum(d)
print(cnt + (n-cnt-1)*cnt)
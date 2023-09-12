import sys
import heapq as h
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
tem = [list(map(int,input().split())) for _ in range(m)]
s,t = map(int,input().split())
for a,b,c in tem:
    arr[a].append((b,c))
    arr[b].append((a,c))
dp = [987654321 for _ in range(n+1)]
def dijkstra(start):
    q = []
    dp[start] = 0
    h.heappush(q,(0,start))
    while q:
        dist,now = h.heappop(q)
        if dp[now] < dist: continue
        for i in arr[now]:
            cost = dist + i[1]
            if cost < dp[i[0]]:
                dp[i[0]] = cost
                h.heappush(q,(cost,i[0]))
dijkstra(s)
print(dp[t])
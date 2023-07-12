import heapq as heq
def dik(dot):
    q = []
    dp[dot][dot] = 0
    heq.heappush(q,(dot,0))
    while q:
        now,dist = heq.heappop(q)
        if dp[dot][now] < dist:
            continue
        for i in arr[now]:
            cost = dist + i[1]
            if dp[dot][i[0]] > cost:
                dp[dot][i[0]] = cost
                heq.heappush(q,(i[0],cost))
n,m,k = map(int,input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    arr[a].append((b,c))

dp = [[987654321] * (n+1) for _ in range(n+1)]
ans = 0
for i in range(1,n+1):
    dik(i)
for i in range(1,n+1):
    ans = max(ans,dp[i][k]+dp[k][i])
print(ans)
n, m = map(int,input().split())
byte = [*map(int,input().split())]
cost = [*map(int,input().split())]
ans = 10001
l = sum(cost)
dp = [0] * (l+1)
for i in range(n):
    a, b = byte[i], cost[i]
    for j in range(l,b-1,-1):
        dp[j] = max(dp[j],dp[j-b]+a)
if not l or not m:
    print(0)
else:
    for i in range(l+1):
        if dp[i] >= m:
            print(i)
            break
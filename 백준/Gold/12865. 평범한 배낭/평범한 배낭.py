n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(tuple(map(int,input().split())))
dp = [0] * (m+1)

for a,b in arr:
    for i in range(m,a-1,-1):
        dp[i] = max(dp[i], dp[i-a] + b)
print(dp[-1])
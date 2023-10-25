import sys;input = sys.stdin.readline
n,m = map(int,input().split())
arr= [int(input()) for _ in range(n)]
dp = [int(1e9)]*(m+1)
dp[m] = 0
for i in range(m,0,-1):
    for j in arr:
        if i-j>=0:
            dp[i-j] = min(dp[i]+1,dp[i-j])
print(dp[0] if dp[0] != int(1e9) else -1) 
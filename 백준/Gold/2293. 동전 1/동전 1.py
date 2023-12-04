import sys;input = sys.stdin.readline
n,m = map(int,input().split())
arr= [int(input()) for _ in range(n)]
dp = [0]*(10001)
dp[0] = 1

for i in arr:
    for j in range(m):
        if j+i <= m:
            dp[j+i] += dp[j]
        else:break
print(dp[m])
n = int(input())
dp = [0] * (n+100)
dp[1] = 1
dp[2] = 1
dp[3] = 1
if n==1:
    print(0)
elif n<=3:
    print(dp[n])
else:
    for i in range(4,n+1):
        if not i%3 and not i%2:
            dp[i] = min(dp[i//3]+1,dp[i//2]+1,dp[i-1]+1)
        elif not i%3 and i%2:
            dp[i] = min(dp[i//3]+1,dp[i-1]+1)
        elif i%3 and not i%2:
            dp[i] = min(dp[i//2]+1,dp[i-1]+1)
        else:
            dp[i] = dp[i-1]+1
    print(dp[n])






arr = [i**2 for i in range(1,226)]
dp = [1e9] * 50001
for i in arr:
    if i<50001:
        dp[i] = 1
for j in range(1,len(dp)):
    for i in arr:
        if 0<=j-i<=50001:
            dp[j] = min(dp[j-i] + 1,dp[j])
n = int(input())
print(dp[n])
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(len(arr[i])):
        dp[i][j] = arr[i][j]
for i in range(n-1,0,-1):
    for j in range(n-1):
        dp[i-1][j] = max(dp[i-1][j] + dp[i][j], dp[i-1][j]+dp[i][j+1])

print(dp[0][0])
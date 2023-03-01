n = int(input())
arr= [[0] * 1002 for _ in range(1002)]
dp = [0] * (n+1)
for i in range(1,n+1):
    a,b,x,y = map(int, input().split())
    for k in range(a,a+x):
        for j in range(b,b+y):
            arr[k][j] = i
for i in range(1002):
    for j in range(1002):
        dp[arr[i][j]] += 1
for i in range(1,n+1):
    print(dp[i])
n = int(input())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)

dp = [0] * 301
dp[0] = arr[0]
if n==1:
    print(arr[0])
elif n==2:
    print(arr[0]+arr[1])
else:
    dp[1] = max(arr[0] + arr[1], arr[1])
    dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])
    for i in range(3, n):
        dp[i] = max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])
    print(dp[n-1])

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
dp = [0] * (n+1)
if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0]+arr[1])
elif n == 3:
    print(max(arr[0] + arr[2], arr[1] + arr[2], arr[0] + arr[1]))
else:
    dp[0] = arr[0]
    dp[1] = max(arr[1], arr[0] + arr[1])
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2], arr[0] + arr[1])

    for i in range(3, n):
        dp[i] = max(arr[i] + arr[i-1] + dp[i-3], arr[i] + dp[i-2], dp[i-1])
    print(max(dp))
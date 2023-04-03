n = int(input())
dp = [0] * (n+100)
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp_str = [0] * (n+100)
dp_str[1] = '1'
dp_str[2] = '2 1'
dp_str[3] = '3 1'
if n==1:
    print(0)
    print(1)
elif n<=3:
    print(dp[n])
    print(dp_str[n])
else:
    for i in range(4,n+1):
        if not i%3 and not i%2:
            dp[i] = min(dp[i//3]+1,dp[i//2]+1,dp[i-1]+1)
            if dp[i//3] == min(dp[i//3],dp[i//2],dp[i-1]):
                dp_str[i] = f'{i}' + " " +dp_str[i//3]
            elif dp[i//2] == min(dp[i//3],dp[i//2],dp[i-1]):
                dp_str[i] = f'{i}' + " " + dp_str[i // 2]
            else:
                dp_str[i] = f'{i}' + " " + dp_str[i-1]
        elif not i%3 and i%2:
            dp[i] = min(dp[i//3]+1,dp[i-1]+1)
            if dp[i//3] == min(dp[i//3],dp[i-1]):
                dp_str[i] = f'{i}' + " " + dp_str[i//3]
            else:
                dp_str[i] = f'{i}' + " " + dp_str[i-1]
        elif i%3 and not i%2:
            dp[i] = min(dp[i//2]+1,dp[i-1]+1)
            if dp[i//2] == min(dp[i//2],dp[i-1]):
                dp_str[i] = f'{i}' + " " + dp_str[i//2]
            else:
                dp_str[i] = f'{i}' + " " + dp_str[i-1]
        else:
            dp[i] = dp[i-1]+1
            dp_str[i] = f'{i}' + " " + dp_str[i-1]
    print(dp[n])
    print(dp_str[n])
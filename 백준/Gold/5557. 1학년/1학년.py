import sys; input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
ans = [[0] * 21 for _ in range(n)]
ans[0][arr[0]] = 1
for i in range(1,n-1):
    for j in range(21):
        if ans[i-1][j]:
            if j + arr[i] <= 20:
                ans[i][j+arr[i]] += ans[i-1][j]
            if j - arr[i] >= 0:
                ans[i][j-arr[i]] += ans[i-1][j]
print(ans[n-2][arr[-1]])
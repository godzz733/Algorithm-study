import sys; input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int,input().split())))
t = sum(arr[1:])
ans = 0
for i in range(n-1):
    ans += t - (n-i-1) * arr[i]
    t -= arr[i+1]
print(ans<<1)
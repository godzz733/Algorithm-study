import sys; input = sys.stdin.readline
n,m = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(n):
    arr[i] = (m - arr[i])
if sum(arr) > m:
    print(0)
    exit()
ans = 1
mod = int(1e9) + 7
for i in arr:
    for j in range(i,0,-1):
        ans *= m
        m -= 1
    for j in range(i,0,-1):
        ans //= j
    ans %= mod

print(ans % mod)
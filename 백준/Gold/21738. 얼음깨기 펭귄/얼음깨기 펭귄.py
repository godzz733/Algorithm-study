import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m,k = map(int,input().split())
arr = [[] for _ in range(n+1)]
dp = [0] * (n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

dp[k] = 1

ans = []

def solve(num,cnt):
    if num <= m:
        ans.append(cnt)
    dp[num] = 1
    for i in arr[num]:
        if dp[i] == 0:
            solve(i,cnt+1)

solve(k,0)
ans.sort()
print(n-ans[0]-ans[1]-1)
import sys; input = sys.stdin.readline

n,m = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(n)]
ans = [0] * (m+1)
for a,b in arr:
    for i in range(m,a-1,-1):
        ans[i] = max(ans[i], ans[i-a]+b)
print(ans[m])
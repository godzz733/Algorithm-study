import sys; input = sys.stdin.readline
n,m = map(int,input().split())
ans = 0
g = [int(1e9),int(1e9)]
for _ in range(m):
    a,b = map(int,input().split())
    g[0] = min(g[0],a)
    g[1] = min(g[1],b)
if g[0] >= g[1]*6:
    ans = g[1]*n
else:
    ans = g[0]*(n//6) + min(g[0],g[1]*(n%6))
print(ans)
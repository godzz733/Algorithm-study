import sys; input = sys.stdin.readline
n,m = map(int,input().split())
ans = 2**31
for _ in range(n):
    a,b,c = map(int,input().split())
    if a + b*(c-1) < m: continue
    else:
        for i in range(c):
            if a + b*i < m: continue
            ans = min(ans, a + b*i - m)
print(ans if ans < 2**31 else -1)
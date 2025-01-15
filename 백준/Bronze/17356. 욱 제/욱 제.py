import sys; input = sys.stdin.readline
a,b = map(int,input().split())
ans = 1/(1+10**((b-a)/400))
print(ans)
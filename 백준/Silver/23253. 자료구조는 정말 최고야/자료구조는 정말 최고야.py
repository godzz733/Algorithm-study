import sys;input = sys.stdin.readline
n,m = map(int,input().split())
ans = "Yes"
for _ in range(m):
    _ = input()
    a = list(map(int,input().split()))
    if sorted(a,reverse=True) != a:ans = "No"
print(ans)
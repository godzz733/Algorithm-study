import sys; input = sys.stdin.readline
a,b,c,d = map(int,input().split())
ans = 0
if c<<1 >= d:
    ans += min(a,b)*d
    if d*2 <= c<<1:
        ans += abs(a-b)//2*(d*2)
        ans += (abs(a-b)%2)*c
    else:
        ans += abs(a-b)*c
else:
    ans += (a+b) * c
print(ans)
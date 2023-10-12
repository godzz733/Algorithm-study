import sys; input = sys.stdin.readline
a,b,c,d = map(int, input().split())
ans = 0
st = 0
fi = max(b,c,d)
for _ in range(10000):
    mid = (st+fi)/2
    if (b//mid) * (c//mid) * (d//mid) >= a:
        ans = max(ans,mid)
        st = mid
    else:
        fi = mid
print(ans)
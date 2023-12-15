import sys;input = sys.stdin.readline
n,m = map(int,input().split())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append((a,b,b-a))
arr.sort()
ans = 0
now = 0
for i in range(n):
    a,b,c = arr[i]
    if a > now:
        ans += c//m+1
        now = a + (c//m+1)*m - 1
        if c%m == 0:
            ans -= 1
            now -= m
    elif a == now:
        c -= 1
        a += 1
        ans += c//m+1
        now = a + (c//m+1)*m - 1
        if c%m == 0:
            ans -= 1
            now -= m
    else:
        a = now+1
        c = b - a
        ans += c//m+1
        now = a + (c//m+1)*m - 1
        if c%m == 0:
            ans -= 1
            now -= m
    # print(ans,now)
print(ans)
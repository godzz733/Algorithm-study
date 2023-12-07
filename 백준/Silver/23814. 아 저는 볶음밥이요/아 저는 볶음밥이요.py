import sys;input = sys.stdin.readline
n = int(input())
a,b,c = map(int,input().split())
_a,_b = n-a%n,n-b%n
m = 0
ans = 0
if _a <= c:
    if not _a:
        m = a//n + b//n + c//n
        ans = c
    else:
        m = a//n + b//n + (c-_a)//n + 1
        ans = c-_a

if _b <= c:
    if not _b:
        tem = a//n + b//n + c//n
        if tem >= m:
            ans = c
            m = tem
    else:
        tem = a//n + b//n + (c-_b)//n + 1
        if tem > m:
            ans = c-_b
            m = tem
        elif tem == m:
            ans = max(ans,c-_b)
            m = tem

if _a + _b <= c:
    if not _a and not _b:
        tem = a//n + b//n + c//n
        if tem >= m:
            ans = c
    else:
        tem = a//n + b//n + (c-_a-_b)//n + 2
        if tem > m:
            ans = c-_a-_b
            m = tem
        elif tem == m:
            ans = max(ans,c-_a-_b)
            m = tem

tem = a//n + b//n + c//n
if tem >= m:
    ans = max(ans,c)
    m = tem
print(ans)
import sys; input = sys.stdin.readline
from math import gcd
a,b,c,d = map(int,input().split())

ans = 0
arr = [(1,i) for i in range(1,c+1)]

def fn2(a,b):
    t = gcd(a,b)
    return (a//t, b//t)

def fn1(x1,x2,num,cnt,j):
    global ans
    if (x1,x2) == (a,b):
        ans += 1
        return
    if cnt == d:
        return
    for i in range(j,c):
        t1,t2 = fn2(x1*arr[i][1]+x2,x2*arr[i][1])
        if num * arr[i][1] > c:
            break
        if a*t2 >= b*t1:
            fn1(t1,t2,arr[i][1]*num,cnt+1,i) 
a,b = fn2(a,b)
fn1(0,1,1,0,0)
print(ans)
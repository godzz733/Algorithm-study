import sys; input = sys.stdin.readline
while 1:
    a,b,c = map(int,input().split())
    if a==0 and b == 0 and c==0:
        break
    ans = [int(1e9),int(1e9)]
    for i in range(50001):
        if not abs(c-a*i) % b:
            t = [i,abs(c-a*i)//b]
            if sum(ans) > sum(t):
                ans = t
            elif sum(ans) == sum(t):
                if ans[0]*a+ans[1]*b > t[0]*a+t[1]*b:
                    ans = t
        if not abs(a*i+c) % b:
            t = [i,abs(c+a*i)//b]
            if sum(ans) > sum(t):
                ans = t
            elif sum(ans) == sum(t):
                if ans[0]*a+ans[1]*b > t[0]*a+t[1]*b:
                    ans = t
    print(*ans)
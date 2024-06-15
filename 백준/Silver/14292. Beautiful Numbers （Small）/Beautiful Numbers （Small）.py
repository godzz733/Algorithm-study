import sys; input = sys.stdin.readline
def solve(t,x):
    num = 0
    while t:
        if t%x == 1:
            num += 1
        else:
            return 0
        t //= x
    return num
for tc in range(int(input())):
    n = int(input())
    ans = [0,0]
    for i in range(2,n+1):
        t = solve(n,i)
        if t > ans[1]:
            ans = [i,t]
    print(f"Case #{tc+1}: {ans[0]}")
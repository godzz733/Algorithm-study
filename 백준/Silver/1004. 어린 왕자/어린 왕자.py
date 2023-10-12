import sys; input = sys.stdin.readline
for _ in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    ans = 0
    for _ in range(n):
        a,b,c = map(int,input().split())
        nx = (x1-a)**2 + (y1-b)**2
        ny = (x2-a)**2 + (y2-b)**2
        nz = c**2
        if nx < nz and ny > nz: ans += 1
        elif nx > nz and ny < nz: ans += 1
    print(ans)
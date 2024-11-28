import sys; input = sys.stdin.readline
for _ in range(int(input())):
    a,b = map(int,input().rstrip().split())
    ans = 0
    w = 0
    now = 0
    for _ in range(b):
        x,y = map(int,input().rstrip().split())
        ans += x - now
        
        if y + w == a:
            ans += x
            now = 0
            w = 0
        elif y + w < a:
            now = x
            w += y
        else:
            ans += x << 1
            now = x
            w = y
    
    print(ans + now)

import sys; input = sys.stdin.readline

while 1:
    a,b,c,d = map(int, input().split())
    if sum([a,b,c,d]) == 0:
        break
    if not a:
        a = d // (b*c)
    elif not b:
        b = d // (a*c)
    elif not c:
        c = d // (a*b)
    else:
        d = a*b*c
    print(a,b,c,d)
import sys; input = sys.stdin.readline
for _ in range(int(input())):
    r, b, m = map(float, input().split())
    r = (r + 100.0) / 100.0
    i = 0
    f = False
    pb = b
    while i < 1200 and not f:
        b = ((int((b * r * 100) + 0.5 + 1e-8) / 100.0) - m)
        if b <= 0:
            break
        if b > pb:
            f = True
        pb = b
        i += 1
    if f or i == 1200:
        print("impossible")
    else:
        print(i + 1)
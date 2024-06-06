import sys; input = sys.stdin.readline
while 1:
    n = input().rstrip()
    ans = [0,0]
    if n == "#": break
    a,b = 0,0
    for i in n:
        if i == "A":
            a += 1
        else:
            b += 1
        if (a >= 4 or b >=4) and abs(a-b) >= 2:
            if a > b:
                ans[0] += 1
            else:
                ans[1] += 1
            a,b = 0,0
    print(f'A {ans[0]} B {ans[1]}')
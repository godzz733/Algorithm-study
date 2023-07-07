for _ in range(int(input())):
    x1,y1,r1,x2,y2,r2 = map(int ,input().split())
    if r1 > r2:
        x1,y1,r1,x2,y2,r2 = x2,y2,r2,x1,y1,r1
    if not r1 or not r2:
        print(0)
        continue
    elif x1==x2 and y1==y2:
        if r1 == r2:
            print(-1)
            continue
        else:
            print(0)
            continue
    else:
        x = (((x1-x2)**2+(y1-y2)**2)**(1/2))
        if x == r1+r2 or x+r1 == r2:
            print(1)
            continue
        elif x > r1+r2 or r2>x+r1:
            print(0)
            continue
        else:
            print(2)
            continue
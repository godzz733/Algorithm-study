n = int(input())
for _ in range(n):
    a_n, *a = map(int,input().split())
    v_n, *b= map(int, input().split())
    for i in range(4,0,-1):
        _a = a.count(i)
        _b = b.count(i)
        if _a < _b:
            print('B')
            break
        elif _a> _b:
            print('A')
            break
        else:
            continue
    else:
        print('D')
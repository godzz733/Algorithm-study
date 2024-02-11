while 1:
    a,b = map(int, input().split())
    if a == 0 and b == 0:
        break
    a,b = max(a,b), min(a,b)
    if a%b == 0:
        print('A wins')
        continue
    arr = []
    while a%b:
        arr.append(a//b)
        a,b = b, a%b
    if len(arr) == 1 and arr[0] == 1:
        print('B wins')
        continue
    now, pre = 0,0
    if arr[-1] == 1:
        now = 'B'
        pre = 'A'
    else:
        now = 'A'
        pre = 'B'
    for i in range(len(arr)-2,0,-1):
        if arr[i] == 1:
            if pre == 'A':
                now = 'A'
                pre = 'B'
            else:
                now = 'B'
                pre = 'A'
        else:
            now = 'A'
            pre = 'B'
    if now == 'A':
        if arr[0] == 1:
            print('B wins')
        else:
            print('A wins')
    else:
        print('A wins')
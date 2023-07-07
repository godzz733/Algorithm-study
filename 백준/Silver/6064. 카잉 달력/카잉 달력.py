for _ in range(int(input())):
    arr = set()
    n,m,a,b = map(int,input().split())
    if n>m:
        n,m,a,b = m,n,b,a
    tem = a
    idx = 1
    arr.add(a)
    while tem + n*idx <= n*m:
        arr.add(tem + n*idx)
        idx += 1
    tem = b
    idx = 1
    ans = -1
    if tem in arr:
        ans = tem
    a = []
    if ans == -1:
        while tem + m*idx <= n*m:
            if tem + m*idx in arr:
                ans = tem + m*idx
                break
            a.append(tem + m*idx)
            idx += 1
    print(ans)
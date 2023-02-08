while 1:
    n, *arr = [*map(int, input().split())]
    if n == 0:
        break
    result = []
    pr = []
    for i in range(1<<n):
        li = []
        for j in range(n):
            if i&(1<<j):
                li.append(arr[j])
        result.append(li)
    for i in result:
        if len(i) == 6:
            pr.append(i)
    pr.sort()
    for i in pr:
        print(*i)
    print()
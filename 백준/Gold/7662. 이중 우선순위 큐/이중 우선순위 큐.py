import heapq
for _ in range(int(input())):
    n = int(input())
    q = [] # 최소힙
    req = [] # 최대힙
    idx = 0
    delset = set()

    for _ in range(n):
        a, b = map(str,input().split())
        if a == 'I':
            heapq.heappush(q,(int(b),idx))
            heapq.heappush(req,(-int(b),idx))
            idx += 1
        else:
            if b == '-1':
                while q:
                    a = heapq.heappop(q)[1]
                    if a not in delset:
                        delset.add(a)
                        break
            else:
                while req:
                    a = heapq.heappop(req)[1]
                    if a not in delset:
                        delset.add(a)
                        break
    result1 = 'fail'
    result2 = 'fail'
    if not q:
        print('EMPTY')
    else:
        while q:
            a = heapq.heappop(q)
            if a[1] not in delset:
                result1 = a[0]
                break
        while req:
            a = heapq.heappop(req)
            if a[1] not in delset:
                result2 = -a[0]
                break
        if result1 == 'fail' and result2 == 'fail':
            print("EMPTY")
        elif result1 == 'fail' and result2 != 'fail':
            print(result2, result2)
        elif result2 == 'fail' and result1 != 'fail':
            print(result1, result1)
        else:
            print(result2, result1)
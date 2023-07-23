def solution(cap, n, deliveries, pickups):
    answer = 0
    arr1 = []
    arr2 = []
    for i in range(n):
        if deliveries[i]: arr1.append([deliveries[i],i+1])
        if pickups[i]: arr2.append([pickups[i],i+1])
    while 1:
        if not arr1 and not arr2: break
        tem = cap
        temidx = 0
        while tem != 0:
            if not arr1:
                break
            temidx = max(temidx,arr1[-1][1])
            if arr1[-1][0] < tem:
                tem -= arr1[-1][0]
                arr1.pop()
            elif arr1[-1][0] == tem:
                tem = 0
                arr1.pop()
            else:
                arr1[-1][0] -= tem
                tem = 0
        tem = cap
        while tem != 0:
            if not arr2:
                break
            temidx = max(temidx,arr2[-1][1])
            if arr2[-1][0] < tem:
                tem -= arr2[-1][0]
                arr2.pop()
            elif arr2[-1][0] == tem:
                tem = 0
                arr2.pop()
            else:
                arr2[-1][0] -= tem
                tem = 0
        answer += temidx
    answer *= 2
        
        
    return answer
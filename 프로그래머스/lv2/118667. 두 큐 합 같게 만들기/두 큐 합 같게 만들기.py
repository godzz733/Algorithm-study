from collections import deque
def solution(queue1, queue2):
    arr1 = deque()
    arr2 = deque()
    for i in queue1:
        arr1.append(i)
    for i in queue2:
        arr2.append(i)
    a = sum(queue1)
    b = sum(queue2)
    _sum = a + b
    cnt = 0
    if _sum % 2:
        return -1
    while (a != b):
        if b > a:
            tem = arr2.popleft()
            a += tem
            b -= tem
            arr1.append(tem)
            cnt += 1
        else:
            tem = arr1.popleft()
            b += tem
            a -= tem
            arr2.append(tem)
            cnt += 1
        if cnt > len(queue1) + len(queue2) + 100000 or not len(arr1) or not len(arr2):
            cnt = -1
            break
    answer = cnt
    return answer

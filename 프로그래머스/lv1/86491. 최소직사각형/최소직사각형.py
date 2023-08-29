def solution(sizes):
    answer = 0
    a = b = 0
    for i in sizes:
        if i[0] > i[1]: i[1],i[0] = i[0],i[1]
        a = max(a,i[0])
        b = max(b,i[1])
    answer = a*b
    return answer
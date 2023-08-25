def solution(s):
    answer = 0
    a = s[0]
    i1 = 1
    i2 = 0
    for i in s[1:]:
        if i1 == 0:
            i1 = 1
            a = i
        elif i != a:
            i2 += 1
            if i1 == i2:
                answer += 1
                i1 = i2 = 0
        else:
            i1 += 1
            if i1 == i2:
                answer += 1
                i1 = i2 = 0
    if i1: answer += 1
    return answer
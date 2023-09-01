def solution(storey):
    answer = 0
    storey = list(map(int,reversed(str(storey)))) + [0]
    for i in range(len(storey)-1):
        if storey[i] >= 10:
            storey[i+1] += 1
            storey[i] %= 10
        if storey[i] <= 4:answer += storey[i]
        elif storey[i]>5: 
            answer += 10-storey[i]
            storey[i+1] += 1
        else:
            answer += 5
            if storey[i+1] > 4:
                storey[i+1] += 1
    answer += storey[-1]
    return answer
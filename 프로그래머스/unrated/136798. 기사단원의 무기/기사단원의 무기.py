def solution(number, limit, power):
    answer = 0
    arr = [0] * (number+1)
    for i in range(1,number+1):
        for j in range(1,number+1):
            if i*j > number: break
            arr[i*j] += 1
    for i in range(1,number+1):
        if arr[i] <= limit:answer += arr[i] 
        else: answer += power
    return answer
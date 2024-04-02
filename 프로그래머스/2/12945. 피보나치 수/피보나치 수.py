def solution(n):
    answer = [1,1]
    for _ in range(n-2):
        answer = [answer[1],sum(answer)%1234567]
    return answer[1]
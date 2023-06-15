def solution(participant, completion):
    dic = {}
    for i in participant:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in completion:
        if dic[i] == 1:
            del dic[i]
        else:
            dic[i] -= 1
    for i in dic.keys():
        answer = i
    return answer
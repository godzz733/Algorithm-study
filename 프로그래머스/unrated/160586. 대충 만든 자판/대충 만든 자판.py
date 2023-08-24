def solution(keymap, targets):
    answer = []
    dic = {}
    for i in keymap:
        for j in range(len(i)):
            if i[j] not in dic: dic[i[j]] = j+1
            else: dic[i[j]] = min(dic[i[j]], j+1)
    for i in targets:
        tem = 0
        for j in i:
            if j not in dic:
                tem = -1
                break
            else : tem += dic[j]
        answer.append(tem)

    return answer
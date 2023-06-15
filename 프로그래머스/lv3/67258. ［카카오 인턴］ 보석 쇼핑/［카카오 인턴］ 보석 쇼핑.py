def solution(gems):
    jew = set(gems)
    size = len(jew)
    st = 0
    fi = 0
    dic = dict()
    ans = (300000,987654321)
    last = -1
    while (st <= fi and fi<len(gems)):
        if last != fi:
            if gems[fi] not in dic:
                dic[gems[fi]] = 1
            else:
                dic[gems[fi]] += 1
        last = fi
        if len(dic) == size:
            if ans[0] > st or ans[1]-ans[0] > fi-st:
                ans = (st,fi)
            if dic[gems[st]] == 1:
                del dic[gems[st]]
            else:
                dic[gems[st]] -= 1
            st += 1
            continue;
        fi += 1
        
    answer = [ans[0]+1,ans[1]+1]
    return answer
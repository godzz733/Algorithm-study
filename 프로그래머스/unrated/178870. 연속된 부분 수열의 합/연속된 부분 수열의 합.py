def solution(sequence, k):
    st = 0
    fi = 0
    ans = 0
    answer = [0,10000000]
    sequence.append(0)
    while st<=fi and fi<len(sequence):
        if ans == k:
            if answer[1]-answer[0] > fi-1-st:
                answer = [st,fi-1]
            elif answer[1]-answer[0] == fi-1-st and st < answer[0]:
                answer = [st,fi-1]
            ans -= sequence[st]
            st += 1
            continue
        if ans < k:
            ans += sequence[fi]
            fi += 1
        elif ans > k:
            ans -= sequence[st]
            st += 1

        

    return answer
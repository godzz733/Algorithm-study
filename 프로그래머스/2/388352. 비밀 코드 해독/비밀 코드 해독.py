from itertools import combinations
def solution(n, q, ans):
    answer = 0
    arr = [i for i in range(1,n+1)]
    for i in combinations(arr,5):
        for j in range(len(q)):
            t = 0
            for k in range(5):
                if i[k] in q[j]:
                    t += 1
            if ans[j] != t:
                break
        else:
            answer += 1
    return answer
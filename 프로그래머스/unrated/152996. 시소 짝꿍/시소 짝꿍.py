def solution(weights):
    answer = 0
    ans = set()
    arr = [set() for _ in range(max(weights)*4 + 1)]
    lst = [0] * (max(weights)+1)
    for i in weights:
        lst[i] += 1
        for j in range(2,5):
            arr[i*j].add(i)
            
    for i in weights:
        for j in range(2,5):
            for k in arr[i*j]:
                ans.add(tuple(sorted([i,k])))

    for i,j in ans:
        if i == j:
            if lst[i] == 1:
                pass
            else:
                answer += lst[i] * (lst[i]-1) // 2
        else:
            answer += lst[i] * lst[j]
    return answer
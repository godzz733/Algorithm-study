n = int(input())
for _ in range(n):
    ori = list(input())
    dic = {}
    for i in range(len(ori)):
        dic[ori[i]] = i
    pattern = list(input())
    find = list(input())
    pattern_set = []
    result = []
    for i in range(len(ori)):
        lst = []
        for j in range(len(pattern)):
            lst.append(ori[(dic[pattern[j]]+i)%len(ori)])
        pattern_set.append(lst)
    for k in range(len(pattern_set)):
        cnt = 0
        j = 0
        pi = [0] * len(pattern_set[k])
        for i in range(1,len(pattern_set[k])):
            while j>0 and pattern_set[k][i] != pattern_set[k][j]:
                j = pi[j-1]
            if pattern_set[k][i] == pattern_set[k][j]:
                pi[i] = j+1
                j += 1
        j = 0
        for i in range(len(find)):
            while j>0 and find[i] != pattern_set[k][j]:
                j = pi[j-1]
            if find[i] == pattern_set[k][j]:
                if j == len(pattern_set[k])-1:
                    cnt += 1
                    j = pi[j]
                    if cnt>1:
                        break
                else:
                    j += 1
        if cnt == 1:
            result.append(k)
    if not result:
        print("no solution")
    elif len(result) == 1:
        print(f'unique: {result[0]}')
    else:
        print(f'ambiguous: ', end='')
        print(*result)

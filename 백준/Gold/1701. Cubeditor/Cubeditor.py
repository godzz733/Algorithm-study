pattern = list(input())
ans = 0
if len(pattern) == 2:
    for i in pattern:
        if pattern.count(i)>1: ans = 1
elif len(pattern) == 3:
    if pattern[0] == pattern[1] and pattern[1] == pattern[2]: ans = 2
else:
    idx = len(pattern)-1
    while idx > 2:
        tem = pattern
        pi = [0] * len(tem)
        j = 0
        for i in range(1,len(tem)):
            while j>0 and pattern[i] != pattern[j]:
                j = pi[j-1]
            if pattern[i] == pattern[j]:
                pi[i] = j+1
                j += 1
        ans = max(ans,max(pi))
        tem.pop(0)
        idx -= 1
        # print(pi)
print(ans)
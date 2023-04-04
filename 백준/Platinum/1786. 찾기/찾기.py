find = [*input()]
pattern = [*input()]
pi = [0] * len(pattern)
j = 0
result = 0
num = []
for i in range(1,len(pattern)):
    while j>0 and pattern[i] != pattern[j]:
        j = pi[j-1]
    if pattern[i] == pattern[j]:
        pi[i] = j+1
        j+=1
j = 0
for i in range(len(find)):
    while j>0 and find[i] != pattern[j]:
        j = pi[j-1]
    if find[i] == pattern[j]:
        if j == len(pattern)-1:
            result += 1
            num.append(i-j+1)
            j = pi[j]
        else:
            j += 1
print(result)
print(*num)
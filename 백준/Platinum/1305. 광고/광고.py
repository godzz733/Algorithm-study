n = int(input())
find = list(input())
j = 0
pi = [0] * len(find)
for i in range(1,len(find)):
    while j>0 and find[i] != find[j]:
        j = pi[j-1]
    if find[i] == find[j]:
        pi[i] = j+1
        j += 1

print(len(find) - pi[-1])
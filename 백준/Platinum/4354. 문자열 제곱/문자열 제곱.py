while 1:
    find = list(input())
    if find[0] == '.':
        break
    pi = [0] * len(find)
    j = 0
    for i in range(1,len(find)):
        while j>0 and find[i] != find[j]:
            j = pi[j-1]
        if find[i] == find[j]:
            pi[i] = j+1
            j+=1
    if not pi[-1]:
        print(1)
    else:
        if not len(find) % (len(find)-pi[-1]):
            print(len(find) // (len(find)-pi[-1]))
        else:
            print(1)
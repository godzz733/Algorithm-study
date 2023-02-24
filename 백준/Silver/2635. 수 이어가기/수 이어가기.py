n = int(input())
result = []
i =0
for i in range(1,n+1):
    lst = [n,i]
    while 1:
        a = lst[-2] - lst[-1]
        if a<0:
            if not result:
                result.append(lst)
                break
            else:
                if len(lst) > len(result[-1]):
                    result[-1] = lst[:]
                    break
                else:
                    break

        else:
            lst.append(a)
print(len(result[-1]))
print(*result[-1])

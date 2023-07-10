n, m = map(int,input().split())
know = set()
tem = list(map(int,input().split()))
for i in tem[1:]:
    know.add(i)
arr = [1] * m
lst= []
for i in range(m):
    tem = list(map(int, input().split()))
    lst.append(tem)
    for j in tem[1:]:
        if j in know:
            arr[i] = 0
            for k in tem[1:]:
                know.add(k)
            break
for _ in range(50):
    for i in range(m):
        if arr[i] == 0:
            continue
        tem = lst[i]
        for j in tem[1:]:
            if j in know:
                arr[i] = 0
                for k in tem[1:]:
                    know.add(k)
                break
print(sum(arr))
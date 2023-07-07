def distance(a,b,c):
    global arr
    tem = 0
    for i in range(4):
        if arr[a][i] != arr[b][i]:
            tem += 1
    for i in range(4):
        if arr[c][i] != arr[b][i]:
            tem += 1
    for i in range(4):
        if arr[a][i] != arr[c][i]:
            tem += 1
    return tem
for _ in range(int(input())):
    n = int(input())
    tem = list(map(str, input().split()))
    ans = 999
    if n>32:
        ans = 0
    if ans:
        dic = {}
        arr = []
        for i in tem:
            if i not in dic:
                dic[i] = 1
                arr.append(i)
            elif dic[i] == 1:
                dic[i] += 1
                arr.append(i)
            else:
                ans = 0
                break
    if ans:
        size = len(arr)
        for i in range(size-2):
            for j in range(i+1,size-1):
                for k in range(j+1,size):
                    ans = min(ans,distance(i,j,k))
    print(ans) 
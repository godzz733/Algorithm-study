import sys
t = int(input())
for _ in range(t):
    dic = {}
    num = int(input())
    for _ in range(num):
        a,b = map(str, sys.stdin.readline().split())
        if b not in dic:
            dic[b] = 1
        else:
            dic[b] +=1
    result = 1
    arr = list(dic.values())
    if len(arr)!=1:
        for i in arr:
            result *= (i+1)
        print(result-1)
    else:
        result = arr[0]
        print(result)

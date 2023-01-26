import sys
a, b = map(int,input().split())
arr = [*map(int, sys.stdin.readline().split())]

arr1 = [*map(int, sys.stdin.readline().split())]
dic = {}
for i in arr:
    dic[i] = 1
for i in arr1:
    if i in dic:
        dic[i] = 0
    else:
        dic[i] = 1

print(sum(list(dic.values())))
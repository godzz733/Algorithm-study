import sys
t1 = int(input())
arr1 = map(int,sys.stdin.readline().split())
t2 = int(input())
arr2 = map(int,sys.stdin.readline().split())
dic = {}
result =[]
for i in arr1:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for j in arr2:
    if j in dic.keys():
        result.append(dic[j])
    else:
        result.append(0)
print(*result)
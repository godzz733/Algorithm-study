import sys
input = sys.stdin.readline
n = int(input())

arr = [*map(int,input().rstrip().split())]
li = []
result = []
result_num = 0
li.append(arr[0])
for i in range(1,n-1):
    if li ==[]:
        li.append(arr[i])
    else:
        if arr[i] <= arr[i-1]:
            result.append(li)
            li = []
            li.append(arr[i])
        else:
            li.append(arr[i])
if li==[]:
    pass
else:
    if li[-1] <arr[n-1]:
        li.append(arr[n-1])
        result.append(li)
    else:
        result.append(li)
for i in result:
    if len(i)!=1:
        result_num = max(result_num,i[-1]-i[0])


print(result_num)
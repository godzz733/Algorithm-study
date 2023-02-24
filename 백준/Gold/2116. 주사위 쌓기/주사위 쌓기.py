import copy
n = int(input())
ori = [list(map(int, input().split())) for _ in range(n)]
lst = [(0,5),(1,3),(2,4),(3,1),(4,2),(5,0)]
result = []
cnt = 0

arr = copy.deepcopy(ori)
a = arr[0][0]
b = arr[0][5]
cnt += max(arr[0][1],arr[0][2],arr[0][3],arr[0][4])
for i in range(1,n):
    a = b
    b = arr[i][lst[arr[i].index(a)][1]]
    arr[i].remove(a)
    arr[i].remove(b)
    cnt += max(arr[i])
result.append(cnt)

arr = copy.deepcopy(ori)
cnt = 0
a = arr[0][1]
b = arr[0][3]
cnt += max(arr[0][0],arr[0][2],arr[0][4],arr[0][5])
for i in range(1,n):
    a = b
    b = arr[i][lst[arr[i].index(a)][1]]
    arr[i].remove(a)
    arr[i].remove(b)
    cnt += max(arr[i])
result.append(cnt)

arr = copy.deepcopy(ori)
cnt = 0
a = arr[0][2]
b = arr[0][4]
cnt += max(arr[0][0],arr[0][1],arr[0][3],arr[0][5])
for i in range(1,n):
    a = b
    b = arr[i][lst[arr[i].index(a)][1]]
    arr[i].remove(a)
    arr[i].remove(b)
    cnt += max(arr[i])
result.append(cnt)

arr = copy.deepcopy(ori)
cnt = 0
a = arr[0][4]
b = arr[0][2]
cnt += max(arr[0][0],arr[0][1],arr[0][3],arr[0][5])
for i in range(1,n):
    a = b
    b = arr[i][lst[arr[i].index(a)][1]]
    arr[i].remove(a)
    arr[i].remove(b)
    cnt += max(arr[i])
result.append(cnt)

arr = copy.deepcopy(ori)
cnt = 0
a = arr[0][5]
b = arr[0][0]
cnt += max(arr[0][1],arr[0][2],arr[0][3],arr[0][4])
for i in range(1,n):
    a = b
    b = arr[i][lst[arr[i].index(a)][1]]
    arr[i].remove(a)
    arr[i].remove(b)
    cnt += max(arr[i])
result.append(cnt)

arr = copy.deepcopy(ori)
cnt = 0
a = arr[0][3]
b = arr[0][1]
cnt += max(arr[0][0],arr[0][2],arr[0][4],arr[0][5])
for i in range(1,n):
    a = b
    b = arr[i][lst[arr[i].index(a)][1]]
    arr[i].remove(a)
    arr[i].remove(b)
    cnt += max(arr[i])
result.append(cnt)
print(max(result))
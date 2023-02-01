
n,m = map(int,input().split())
arr = []
li = []
result = []
num = 0
cnt = 0
for _ in range(n):
    li = [*map(int,input().split())]
    arr.append(li)
    li = []
arr.sort(key=lambda x:(x[1],x[2],x[3]),reverse=True)
li.append(arr[0][0])
for i in range(1,n):
    if li==[]:
        li.append(arr[i][0])
    elif arr[i][1]<arr[i-1][1]:
        result.append(li)
        li = []
        li.append(arr[i][0])
    elif arr[i][1]==arr[i-1][1] and arr[i][2]<arr[i-1][2]:
        result.append(li)
        li = []
        li.append(arr[i][0])
    elif arr[i][1]==arr[i-1][1] and arr[i][2]==arr[i-1][2] and arr[i][3]<arr[i-1][3]:
        result.append(li)
        li = []
        li.append(arr[i][0])
    elif arr[i][1]==arr[i-1][1] and arr[i][2]==arr[i-1][2] and arr[i][3]==arr[i-1][3]:
        li.append(arr[i][0])

if li!=[]:
    result.append(li)

for i in range(len(result)):
    if m in result[i]:
        idx = i
for i in range(0,idx):
    cnt += len(result[i])
print(cnt+1)
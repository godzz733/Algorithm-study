t= int(input())
arr = []
for i in range(t):
    a,b = map(int, input().split())
    arr.append((a,b))
result = []
count = 0
for k in range(1,len(arr)):
    if arr[0][0]<arr[k][0] and arr[0][1]<arr[k][1]:
        count+=1
result.append(count+1)

for i in range(1,len(arr)):
    count = 0
    arr[0],arr[i] = arr[i],arr[0]
    for k in range(1,len(arr)):
        if arr[0][0]<arr[k][0] and arr[0][1]<arr[k][1]:
            count+=1
        else:
            continue

    result.append(count+1)


for i in range(len(result)-1):
    print(result[i],end=' ')
print(result[-1])



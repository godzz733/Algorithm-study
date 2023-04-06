def binary(cnt,start,end):
    res = 0
    res1 = 0
    while start<=end:
        mid = (start+end)//2
        if cnt + arr[mid] <0:
            start = mid + 1
            res1 = mid
        else:
            end = mid - 1
            res = mid
            if cnt + arr[mid] == 0:
                return mid
    if abs(cnt+arr[res])<abs(cnt+arr[res1]):
        return res
    else:
        return res1
n = int(input())
arr = sorted(list(map(int,input().split())))
acid = -1
base = -1
for i in range(n):
    if arr[i] < 0 :
        base = i
        break
for i in range(n):
    if arr[i] > 0:
        acid = i
        break
result = 3000000001
pri = [0,0,0]
if base == -1:
    print(arr[0],arr[1],arr[2])
elif acid == -1:
    print(arr[-3],arr[-2],arr[-1])
else:
    for i in range(n-2):
        for j in range(i+1,n-1):
            idx = binary(arr[i]+arr[j],j+1,n-1)
            if abs(arr[i]+arr[j]+arr[idx]) < result:
                result = abs(arr[i]+arr[j]+arr[idx])
                pri[0] = arr[i]
                pri[1] = arr[j]
                pri[2] = arr[idx]
    print(*sorted(pri))
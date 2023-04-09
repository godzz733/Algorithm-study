def binary(x,st,end,size):
    res = -1
    while st<=end:
        mid = (st+end)//2
        if dp[mid] < x:
            st = mid + 1
        else:
            res = mid
            end = mid-1
    if st==size:
        return -1
    else:
        return res
lis = 0
n = int(input())
arr = list(map(int,input().split()))
dp = [-1000000001] * n
for i in range(n):
    idx= binary(arr[i],0,lis,lis+1)
    if idx == -1:
        dp[lis] = arr[i]
        lis += 1
    else:
        dp[idx] = arr[i]

print(lis)
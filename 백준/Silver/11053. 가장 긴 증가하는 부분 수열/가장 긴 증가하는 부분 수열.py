def binary(x, start, end, size):
    res = -1
    while start <= end:
        mid = (start + end) // 2
        if dp[mid] < x:
            start = mid + 1
        else:
            res = mid
            end = mid - 1
    if start == size:
        return -1
    return res


n = int(input())
arr = list(map(int, input().split()))
dp = [-1000000001] * n
lis = 0
result_idx = 0
result = []
for i in range(n):
    idx = binary(arr[i], 0, lis, lis + 1)
    if idx == -1:
        dp[lis] = arr[i]
        result_idx = i
        lis += 1
    else:
        dp[idx] = arr[i]

result.append(arr[result_idx])
last = arr[result_idx]
idx = lis-1
for i in range(result_idx-1,-1,-1):
    if arr[i] < last and arr[i] >= dp[idx-1]:
        result.append(arr[i])
        last = arr[i]
        idx -= 1
print(lis)



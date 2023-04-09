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
result = [0] * n
for i in range(n):
    idx = binary(arr[i], 0, lis, lis + 1)
    if idx == -1:
        dp[lis] = arr[i]
        result[i] = lis +1
        lis += 1
    else:
        dp[idx] = arr[i]
        result[i] = idx+1
lst = []
idx = lis
for i in range(n-1,-1,-1):
    if result[i] == idx:
        lst.append(arr[i])
        idx -= 1

print(lis)
print(*lst[::-1])
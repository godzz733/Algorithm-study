n = int(input())


dp = [False] * (n+100)
dp[1] = True
arr = []
for i in range(2,n+1):
    if not dp[i]:
        arr.append(i)
        for j in range(i,n+1,i):
            dp[j] = True
st = 0
end = 1
num = 2
result = arr.count(n)
while st<end and end<len(arr):
    if num == n:
        result += 1
        num -= arr[st]
        st += 1
        continue

    if num < n:
        num += arr[end]
        end += 1
    else:
        num -= arr[st]
        st += 1
if n == 1:
    result = 0
print(result)
n, m = map(int,input().split())
arr = [*map(int,input().split())]
temp = set()
arr.sort()
dp = [0] * (400001)
dp_num = [0] * 400001
for i in range(m-1):
    for j in range(i+1,m):
        if 0<=arr[i]+arr[j]<=799994:
            temp.add(arr[i]+arr[j])
            if not dp[arr[i]+arr[j]]:
                dp[arr[i]+arr[j]] = (i,j)
            dp_num[arr[i]+arr[j]] += 1

lst = sorted(list(temp))
st = 0
end = len(lst) -1
result = 'NO'
while st<end:
    if lst[st] + lst[end]<n:
        st += 1
    else:
        end -= 1
    if lst[st] + lst[end] == n:
        if dp_num[lst[st]] > 1 or dp_num[lst[end]] > 1:
            result = 'YES'
            break
        else:
            if dp[lst[st]][0] != dp[lst[end]][0] and dp[lst[st]][0] != dp[lst[end]][1] and dp[lst[st]][1] != dp[lst[end]][0] and dp[lst[st]][1] != dp[lst[end]][1]:
                result = 'YES'
                break

print(result)
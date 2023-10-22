import sys; input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(int(input()) for _ in range(m))
ans = [0,0]
arr.sort()
for i in range(m):
    if (len(arr)-i) > n:
        if ans[1] < n*arr[i]:
            ans[0] = arr[i]
            arr[1] = n*arr[i]
    else:
        if ans[1] < (len(arr)-i) * arr[i]:
            ans[0] = arr[i]
            ans[1] = (len(arr)-i) * arr[i]
print(*ans)
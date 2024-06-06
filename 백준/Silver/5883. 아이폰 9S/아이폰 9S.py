import sys; input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
ans = 0
for i in range(n):
    t = arr[i]
    now = arr[0]
    tem = 1
    for j in arr[1:]:
        if j == t:
            continue
        if now == j:
            tem += 1
        else:
            ans = max(ans,tem)
            tem = 1
            now = j
    ans = max(ans,tem)
print(ans)
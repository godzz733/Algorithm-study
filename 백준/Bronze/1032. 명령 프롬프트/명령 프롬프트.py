import sys;input = sys.stdin.readline
n = int(input())
arr = list(input().rstrip() for _ in range(n))
l = len(arr[0])
num = [0] * l
for i in range(n):
    for j in range(l):
        if arr[i][j] == arr[0][j]:
            num[j] += 1
ans = ''
for i in range(l):
    if num[i] == n:
        ans += arr[0][i]
    else:
        ans += '?'
print(ans)
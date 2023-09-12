import sys;input = sys.stdin.readline
n,m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
ans = 0
for i in range(n):
    tem = 0
    for j in range(m):
        if arr[i][j] == '|':
            if tem:
                ans += 1
                tem = 0
        else:
            tem += 1
    if tem:
        ans += 1
        tem = 0
for i in range(m):
    tem = 0
    for j in range(n):
        if arr[j][i] == '-':
            if tem:
                ans += 1
                tem = 0
        else:
            tem += 1
    if tem:ans += 1
print(ans)
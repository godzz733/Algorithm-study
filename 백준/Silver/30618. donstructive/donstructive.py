import sys; input = sys.stdin.readline

n = int(input())
ans = [0] * n
if n & 1:
    ans[n//2] = n
    idx = n -1
    for i in range(n//2+1,n):
        ans[i] = idx
        ans[n-1-i] = idx - 1
        idx -= 2
else:
    idx = n
    for i in range(n//2,n):
        ans[i] = idx
        ans[n-1-i] = idx - 1
        idx -= 2
print(*ans)
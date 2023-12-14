import sys;input = sys.stdin.readline
n = int(input())
k = int(input())
ans = 0
for i in range(1,n+1):
    idx = 2
    while i != 1:
        if i % idx == 0:
            i //= idx
        else:
            idx += 1
        if idx > k:
            break
    if idx <= k:
        ans += 1
if k == 1:
    ans = 1
print(ans)
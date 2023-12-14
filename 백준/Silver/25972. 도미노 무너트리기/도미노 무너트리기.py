import sys;input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a,b))
arr.sort()
ans = 0
idx = 0
tem = 0
while idx<n:
    ans += 1
    while idx<n:
        tem = sum(arr[idx])
        idx += 1
        if idx<n and tem>=arr[idx][0]:
            continue
        else:break
print(ans)
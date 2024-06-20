import sys; input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort()
tarr = [[0] for _ in range(10001)]
for a,b,c in arr:
    for j in range(b,c):
        tarr[j].append(a)
ans = 0

for a,b,c in arr:
    ans += a - tarr[b][tarr[b].index(a)-1]
    ans += a - tarr[c-1][tarr[c-1].index(a)-1]
print(ans)
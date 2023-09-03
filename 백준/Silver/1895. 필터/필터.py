import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
t = int(input())
ans = 0
for i in range(n-2):
    for j in range(m-2):
        tem = []
        for k in range(3):
            tem += arr[i+k][j:j+3]
        if sorted(tem)[4] >= t: ans += 1
print(ans)
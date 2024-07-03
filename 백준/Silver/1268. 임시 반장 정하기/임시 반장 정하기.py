import sys; input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
num = 0

lst = [[set() for _ in range(9)] for _ in range(5)]

for i in range(n):
    for j in range(5):
        lst[j][arr[i][j]-1].add(i)
for i in range(n):
    t = set()
    for j in range(5):
        t |= lst[j][arr[i][j]-1]
    if len(t) > num:
        num = len(t)
        ans = i+1
print(ans)
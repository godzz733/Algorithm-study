import sys; input = sys.stdin.readline

a,b,c,d = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(a)]
ans = []
for i in range(a):
    t = ""
    for j in range(b):
        t += arr[i][j]*d
    ans.append(t)

for i in range(a):
    for _ in range(c):
        print(ans[i])
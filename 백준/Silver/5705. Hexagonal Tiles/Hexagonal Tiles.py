import sys; input = sys.stdin.readline
ans = [0] * 41
ans[1] = 1
ans[2] = 2
for i in range(3, 41):
    ans[i] = ans[i - 1] + ans[i - 2]

while 1:
    n = int(input())
    if n == 0:
        break
    print(ans[n])
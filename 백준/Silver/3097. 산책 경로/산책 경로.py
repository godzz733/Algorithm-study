import sys; input = sys.stdin.readline
n = int(input())
arr = [[],[]]
for _ in range(n):
    a,b = map(int, input().split())
    arr[0].append(a)
    arr[1].append(b)
ans = [sum(arr[0]), sum(arr[1])]
print(*ans)
ans.append(1e9)
for i in range(n):
    tem = (ans[0]-arr[0][i])**2 + (ans[1]-arr[1][i])**2
    if ans[2] > tem:
        ans[2] = tem

print("{:.2f}".format(round(ans[2] ** 0.5, 2)))
import sys;input = sys.stdin.readline
n = int(input())
arr = [[] for _ in range(n)]
for i in range(n):
    tem = input()
    for j in range(n):
        if tem[j] == 'Y' and i != j:
            arr[i].append(j)
ans = 0
for i in range(n):
    tem = set()
    for j in arr[i]:
        tem.add(j)
        for k in arr[j]:
            tem.add(k)
    ans = max(ans, len(tem)-1)
print(ans)
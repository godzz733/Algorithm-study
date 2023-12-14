import sys;input = sys.stdin.readline
n = int(input())
arr = [input().rstrip() for _ in range(n)]
ans = [[] for _ in range(n)]
arr.sort(key=lambda x: len(x),reverse=True)
for i in range(n):
    for j in range(n):
        if not ans[j]:
            ans[j].append(arr[i])
            break
        for k in range(len(ans[j])):
            if arr[i] in ans[j][k][:len(arr[i])]:
                break
        else:
            ans[j].append(arr[i])

print(max(map(len,ans)))
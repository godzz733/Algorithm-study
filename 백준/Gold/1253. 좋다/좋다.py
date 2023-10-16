import sys;input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
ans = {}
for i in range(n-1):
    for j in range(i+1,n):
        if arr[i]+arr[j] in ans:
            ans[arr[i]+arr[j]].append((i,j))
        else:
            ans[arr[i]+arr[j]] = [(i,j)]
num = 0
for i in range(n):
    if arr[i] in ans:
        for j,k in ans[arr[i]]:
            if i != j and i != k:
                num += 1
                break
print(num)
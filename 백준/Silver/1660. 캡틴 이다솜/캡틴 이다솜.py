import sys; input = sys.stdin.readline

n = int(input())
arr = [1]
for i in range(2,10000):
    if arr[-1] + i > n:
        break
    arr.append(arr[-1] + i)
for i in range(1,len(arr)):
    arr[i] += arr[i-1]
t = []
for i in arr:
    if i > n: break
    t.append(i)
ans = [100000] * (n+1)
ans[0] = 0
for i in range(1,n+1):
    for j in t:
        if j > i: break
        if ans[i] > ans[i-j] + 1:
            ans[i] = ans[i-j] + 1
print(ans[n])
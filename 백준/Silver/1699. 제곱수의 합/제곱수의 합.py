import sys; input = sys.stdin.readline

n = int(input())
arr = [i**2 for i in range(2,318)]
ans = [i for i in range(n+1)]
idx= 0
for i in range(1,n+1):
    for j in arr:
        if j > i:
            break
        if ans[i] > ans[i-j]+1:
            ans[i] = ans[i-j]+1

print(ans[n])
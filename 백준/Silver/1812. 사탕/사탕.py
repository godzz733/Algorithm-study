import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
lst = arr[::]
for i in range(1,n):lst[i] = -lst[i-1] + arr[i]
ans = [lst[-1]>>1]
print(ans[0])
for i in range(n-1):
    tem = arr[i] - ans[-1]
    ans.append(tem)
    print(tem)
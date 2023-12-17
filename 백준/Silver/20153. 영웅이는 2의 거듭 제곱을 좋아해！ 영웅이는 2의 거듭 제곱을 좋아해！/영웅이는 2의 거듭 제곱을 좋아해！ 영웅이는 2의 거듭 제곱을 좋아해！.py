import sys;input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = 0
lst = 0
for i in arr:
    lst ^= i
ans = max(ans, lst)
for i in range(n):
    ori = lst
    ori ^= arr[i]
    ans = max(ans, ori)
print(str(ans)*2)
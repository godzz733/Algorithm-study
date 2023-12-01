import sys; input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
s = sum(arr)
ans = 0
s1 = s-arr[-1]
num = [0] * (1000000+1)
for i in arr:
    num[i] += 1
num[arr[-1]] -= 1
for i in set(arr[:-1]):
    if s1-i-arr[-1] >= 0 and s1-i-arr[-1] <= 1000000 and num[s1-i-arr[-1]]:
        if s1-i-arr[-1] == i:
            ans += num[s1-i-arr[-1]] * (num[s1-i-arr[-1]]-1)
            continue
        ans += num[s1-i-arr[-1]] * num[i]
ans //= 2
num[arr[-2]] -= 1
s2 = s1-arr[-2]
if s2-arr[-2] <= 1000000 and s2-arr[-2] >= 0:
    ans += num[s2-arr[-2]]

if s2-arr[-3] == arr[-3]:
    ans += 1
print(ans)
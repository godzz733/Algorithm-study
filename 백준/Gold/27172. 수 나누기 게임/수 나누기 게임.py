import sys;input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = [0] * 1000001
_set = set(arr)
_max = max(arr)
for i in arr:
    tem = i * 2
    while tem <= _max:
        if tem in _set:
            ans[i] += 1
            ans[tem] -= 1
        tem += i
for i in arr:
    print(ans[i], end = ' ')
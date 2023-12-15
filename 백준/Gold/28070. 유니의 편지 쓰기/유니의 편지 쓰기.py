import sys;input = sys.stdin.readline
from collections import deque
n = int(input())
arr = [0] * 300000
for _ in range(n):
    a,b = map(str,input().split())
    _a = a.split('-')
    _b = b.split('-')
    arr[int(_a[0])*12+int(_a[1])] += 1
    arr[int(_b[0])*12+int(_b[1])+1] -= 1

for i in range(2000*12,300000):
    arr[i] += arr[i-1]
ans = arr.index(max(arr))
if ans % 12 == 0:
    print(str(ans//12-1)+'-12')
else:
    print(str(ans//12)+'-'+str(ans%12).zfill(2))
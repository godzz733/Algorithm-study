import sys;input = sys.stdin.readline
from itertools import permutations
n,m = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0
def find():
    tem = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] and arr[j] and arr[i] < arr[j]:
                tem += 1
    return tem
lst = []
idx = []
t = [0] * (n+1)
for i in range(n):
    if arr[i]:
        t[arr[i]] = 1
    else:
        idx.append(i)
for i in range(1,n+1):
    if not t[i]:
        lst.append(i)
for i in permutations(lst):
    for j in range(len(i)):
        arr[idx[j]] = i[j]
    if find() == m:ans+=1
    for j in range(len(i)):
        arr[idx[j]] = 0
print(ans)
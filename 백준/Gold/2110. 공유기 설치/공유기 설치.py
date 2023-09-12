import sys
import heapq as q
input = sys.stdin.readline
n,m = map(int,input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
st = 0 
fi = 1000000000
def binary(x):
    idx = 0
    cnt = 1
    tem = arr[idx]
    for i in range(idx+1,n):
        if arr[i] - tem >= x:
            cnt += 1
            tem = arr[i]
    return cnt
while st <= fi:
    mid = (st+fi) >> 1
    tem = binary(mid)
    if tem < m:fi = mid - 1
    else:st = mid+1
print(st-1)
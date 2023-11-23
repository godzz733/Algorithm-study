import sys; input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))

ans = int(1e9)
st = max(arr)
fi = sum(arr)
_sum = sum(arr)
def check(x):
    cnt = 0
    key = 0
    idx = 0
    for i in range(n):
        if cnt + arr[i] > x:
            cnt = 0
            key += 1
        cnt += arr[i]
    if cnt: key += 1
    return key <= m
        
while st<=fi:
    mid = (st+fi) >> 1
    if check(mid):
        ans = min(ans,mid)
        fi = mid - 1
    else:
        st = mid + 1
print(ans)
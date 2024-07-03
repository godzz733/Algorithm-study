import sys; input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
ans = 0

def bisect(x,idx):
    l,r = idx+1,n-1
    while l <= r:
        mid = (l+r) >> 1
        if arr[mid] * 0.9 > x:
            r = mid - 1
        else:
            l = mid + 1
    return l - idx - 1

for i in range(n-1):
    ans += bisect(arr[i],i)
print(ans)
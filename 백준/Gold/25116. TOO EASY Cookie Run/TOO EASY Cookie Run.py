import sys; input = sys.stdin.readline
n,m,k = map(int,input().split())
arr = list(map(int,input().split()))
ans = -1
def solve(x):
    st = 0
    fi = 0
    num = 0
    t = 0
    while st < n:
        if num < m:
            if fi == n:
                break 
            num += arr[fi] + x
            fi += 1
        else:
            t += n - fi + 1
            num -= arr[st] + x
            st += 1
        if fi == n + 1:
            break
    if t >= k:
        return True
    return False
st = 0
fi = m
while st <= fi:
    mid = (st+fi) >> 1
    if solve(mid):
        ans = mid
        fi = mid - 1
    else:
        st = mid + 1
print(ans)
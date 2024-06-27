import sys; input = sys.stdin.readline
n,m = map(int, input().split())
arr = [[] for _ in range(n)]
for i in range(m):
    tem = list(map(int, input().split()))
    for j in range(len(tem)):
        arr[j].append(tem[j])
ans = [0] * n
num = 0

def solve(arr):
    a,b = 0,sum(arr)
    ans = int(1e15) + 1
    res = -1
    for i in range(m):
        a += arr[i]
        b -= arr[i]
        if i == m - 1:
            l,r = arr[i], arr[i]+1
        else:
            l,r = arr[i], arr[i+1] - 1
        _min1 = abs(b-a-(m - 2 * i - 2) * l)
        _min2 = abs(b-a-(m - 2 * i - 2) * r)

        if _min1 < _min2:
            if _min1 < ans:
                ans = _min1
                res = l
        else:
            if _min2 < ans:
                ans = _min2
                res = r
    return ans,res

for i in range(n):
    res, ans[i] = solve(sorted(arr[i]))
    num += res
print(num)
print(*ans)
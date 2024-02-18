import sys; input = sys.stdin.readline
n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k]+arr[k][j])

v = set()
v.add(m)
ans = 987654321
def back(idx,cnt):
    global ans
    if len(v) == n:
        ans = min(ans, cnt)
        return
    for i in range(n):
        if i not in v:
            v.add(i)
            cnt += arr[idx][i]
            if cnt < ans:
                back(i,cnt)
            v.remove(i)
            cnt -= arr[idx][i]
back(m,0)
print(ans)
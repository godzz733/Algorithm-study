import sys; input = sys.stdin.readline
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
a,b,c,d = map(int,input().split())
if a > c:
    a,c = c,a
if b > d:
    b,d = d,b
ans = [[-int(1e9)] * m for _ in range(n)]
ans[0][0] = arr[0][0]
for i in range(n):
    for j in range(m):
        if i-1 >=0:
            if i == a and (j >= b and j<d): continue
            ans[i][j] = max(ans[i][j],ans[i-1][j] + arr[i][j])
        if j-1 >=0:
            if j == b and (i >= a and i<c): continue
            ans[i][j] = max(ans[i][j],ans[i][j-1] + arr[i][j])
print(ans[i][j] if ans[i][j] != -int(1e9) else 'Entity')
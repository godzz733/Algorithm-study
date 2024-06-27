import sys; input = sys.stdin.readline
n,m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
ans = []
def solve(x,y,cnt):
    for i in range(x-1,x-cnt-1,-1):
        if arr[i][y] != '*':
            return -1,-1,-1
    for i in range(x+1,x+cnt+1):
        if arr[i][y] != '*':
            return -1,-1,-1
    for i in range(y-1,y-cnt-1,-1):
        if arr[x][i] != '*':
            return -1,-1,-1
    for i in range(y+1,y+cnt+1):
        if arr[x][i] != '*':
            return -1,-1,-1
    return [x+1,y+1,cnt]

for x in range(n):
    for y in range(m):
        if arr[x][y] == '*':
            for i in range(49,0,-1):
                if x-i < 0 or x+i >= n or y-i < 0 or y+i >= m:
                    pass
                else:
                    if solve(x,y,i) != (-1,-1,-1):
                        ans.append(solve(x,y,i))
                        break
tem = [['.'] * m for _ in range(n)]

for x,y,cnt in ans:
    x -= 1
    y -= 1
    for i in range(x-cnt,x+cnt+1):
        tem[i][y] = '*'
    for i in range(y-cnt,y+cnt+1):
        tem[x][i] = '*'

if tem != arr:
    print(-1)
    exit()
print(len(ans))
for i in ans:
    print(*i)

import sys; input = sys.stdin.readline
n,m = map(int,input().split())
arr = [list(input().rstrip()) for _ in range(n)]
a,b,c,d = 1000,0,1000,0
for i in range(n):
    for j in range(m):
        if arr[i][j] == '#':
            a = min(a,i)
            b = max(b,i)
            break
for i in range(m):
    if arr[a][i] == '#':
        c = min(c,i)
        d = max(d,i)

if arr[a][(d+c)//2] == '.':
    print("UP")
elif arr[b][(d+c)//2] == '.':
    print("DOWN")
elif arr[(a+b)//2][c] == '.':
    print("LEFT")
else:
    print("RIGHT")
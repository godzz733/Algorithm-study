import sys; input = sys.stdin.readline
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
ans = int(1e9)

for i in range(1,(1<<n)-1):
    t1,t2 = 0,0
    tarr = [0] * n
    for j in range(n):
        if i & (1<<j):
            tarr[j] = 1
    for x in range(n-1):
        for y in range(x+1,n):
            if not tarr[x] and not tarr[y]:
                t2 += arr[x][y] + arr[y][x]
            elif tarr[x] and tarr[y]:
                t1 += arr[x][y] + arr[y][x]

    ans = min(ans,abs(t1-t2))

print(ans)
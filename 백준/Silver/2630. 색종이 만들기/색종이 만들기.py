def divide(x,y,n):
    ori = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j] != ori:
                ori = -1
                break
    if ori != -1:
        ans[ori] += 1
        return
    else:
        divide(x,y,n//2)
        divide(x+n//2,y,n//2)
        divide(x,y+n//2,n//2)
        divide(x+n//2,y+n//2,n//2)
        return
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
ans = [0,0]
divide(0,0,n)
print(ans[0])
print(ans[1])
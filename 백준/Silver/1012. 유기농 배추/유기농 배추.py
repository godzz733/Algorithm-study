import sys
sys.setrecursionlimit(100000)
t = int(input())
for _ in range(t):
    count = 0
    m,n,k = map(int,input().split())
    arr = [[0 for i in range(m)] for k in range(n)]
    for _ in range(k):
        a,b = map(int,input().split())
        arr[b][a] = 1
    def baechu(x,y):
        if x<0 or x>=n or y<0 or y>=m:
            return False
        
        if arr[x][y]==1:
            arr[x][y]=0
            baechu(x+1,y)
            baechu(x,y+1)
            baechu(x-1,y)
            baechu(x,y-1)
            return True
        return False

    for i in range(m):
        for j in range(n):
            if baechu(j,i)==True:
                count += 1
    print(count)


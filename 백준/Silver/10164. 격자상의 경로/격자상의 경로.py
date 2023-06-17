n, m, k = map(int,input().split())
arr = [[0] * m for _ in range(n)]
if k != 0:
    a= k//m
    b = k%m -1
    for i in range(a+1):
        arr[i][0] = 1
    for i in range(b+1):
        arr[0][i] = 1
    for i in range(a,n):
        arr[i][b] = 1
    for i in range(b,m):
        arr[a][i] = 1
    
    for i in range(1,a+1):
        for j in range(1,b+1):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
    for i in range(a+1,n):
        for j in range(b+1,m):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
    print(arr[a][b] * arr[n-1][m-1])
else:
    for i in range(n):
        for j in range(m):
            arr[i][j] = 1
    for i in range(1,n):
        for j in range(1,m):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
    print(arr[n-1][m-1])


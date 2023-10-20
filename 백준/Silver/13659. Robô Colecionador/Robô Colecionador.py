import sys;input = sys.stdin.readline
while 1:
    n,m,k = map(int,input().rstrip().split())
    if n == 0:break
    arr = [list(input().rstrip()) for _ in range(n)]
    d = 0
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    x,y = 0,0
    for i in range(n):
        for j in range(m):
            tem = arr[i][j]
            if arr[i][j] not in ['.','*','#']:
                if tem == 'N':d = 0
                elif tem == 'S':d = 2
                elif tem == 'L': d= 1
                else: d = 3
                arr[i][j] = '.'
                x = i
                y = j
            else:
                if tem == '*':arr[i][j] = 1
                elif tem == '#':arr[i][j] = 0
                else:arr[i][j] = 2
    ans = 0
    for i in input().rstrip():
        if i == 'D':
            d = (d+1)%4
        elif i == 'E':
            if d == 0: d = 3
            else: d -= 1
        else:
            nx = x + dx[d]
            ny = y + dy[d]
            if nx <0 or nx>=n or ny<0 or ny>=m or arr[nx][ny] == 0: continue
            if arr[nx][ny] == 1:
                ans += 1
                arr[nx][ny] = 2
            x = nx
            y = ny
    print(ans)
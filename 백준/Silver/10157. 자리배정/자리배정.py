n, m = map(int, input().split())
t = int(input())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
arr = [[0] * n for _ in range(m)]
i = 1
x , y = m-1, 0
c = 0
if t>n*m:
    print(0)
else:
    while 1:
        arr[x][y] = i
        if arr[x][y] == t:
            break
        x += dx[c]
        y += dy[c]
        i += 1

        if x<0 or x>=m or y<0 or y>=n or arr[x][y]:
            x -= dx[c]
            y -= dy[c]
            c += 1
            c %= 4
            i -= 1
            continue
    print(y+1,m-x)
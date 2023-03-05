dx = [-1,0,1,0]
dy = [0,1,0,-1]
cnt = 0
n, m = map(int, input().split())
x,y,d = map(int,input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
def check(x,y):
    cnt = 0
    for i in range(4):
        try:
            if not arr[x+dx[i]][y+dy[i]]:
                cnt += 1
        except:
            continue
    return cnt
def robot(a,b,d):
    global cnt
    x, y = a, b
    while 1:
        if not arr[x][y]:
            cnt += 1
            arr[x][y] = 2
            continue
        elif not check(x,y):
            x -= dx[d]
            y -= dy[d]
            if x<0 or x>=n or y<0 or y>=m or arr[x][y] == 1:
                return
        else:
            d += 3
            d %= 4
            if x+dx[d] <0 or x+dx[d] >=n or y+dy[d] <0 or y+dy[d] >=m:
                continue
            if not arr[x+dx[d]][y+dy[d]]:
                x += dx[d]
                y += dy[d]

robot(x,y,d)
print(cnt)
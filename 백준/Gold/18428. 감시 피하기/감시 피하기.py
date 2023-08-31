import sys
n = int(input())
arr = [list(map(str,input().split())) for _ in range(n)]
wall = set()
def can_make_wall(x,y):
    global wall
    for i in range(x-1,-1,-1):
        if not arr[i][y]:
            wall.add((i,y))
    for i in range(x+1,n):
        if not arr[i][y]:
            wall.add((i,y))
    for i in range(y-1,-1,-1):
        if not arr[x][i]:
            wall.add((x,i))
    for i in range(y+1,n):
        if not arr[x][i]:
            wall.add((x,i))
def ans(x,y):
    for i in range(x-1,-1,-1):
        if arr[i][y] == 2: break
        if arr[i][y] == 1: return 1
    for i in range(x+1,n):
        if arr[i][y] == 2: break
        if arr[i][y] == 1: return 1
    for i in range(y-1,-1,-1):
        if arr[x][i] == 2: break
        if arr[x][i] == 1: return 1
    for i in range(y+1,n):
        if arr[x][i] == 2: break
        if arr[x][i] == 1: return 1
    return 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'X': arr[i][j] = 0
        elif arr[i][j] == 'S': arr[i][j] = 1
        else:arr[i][j] = -1

for i in range(n):
    for j in range(n):
        if arr[i][j] == -1:
            can_make_wall(i,j)
wall = list(wall)
wall.sort()
size = len(wall)
for i in range(size-2):
    arr[wall[i][0]][wall[i][1]] = 2
    for j in range(i+1,size-1):
        arr[wall[j][0]][wall[j][1]] = 2
        for k in range(j+1,size):
            arr[wall[k][0]][wall[k][1]] = 2
            cnt = 0
            for x in range(n):
                for y in range(n):
                    if arr[x][y] == -1:
                        if ans(x,y): cnt += 1
            if not cnt:
                print('YES')
                sys.exit()  
            arr[wall[k][0]][wall[k][1]] = 0
        arr[wall[j][0]][wall[j][1]] = 0
    arr[wall[i][0]][wall[i][1]] = 0
print('NO')
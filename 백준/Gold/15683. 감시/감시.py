import copy
n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
cctv = []
direction = []
result = 100
for i in range(n):
    for j in range(m):
        if 0<lst[i][j]<6:
            cctv.append((i,j,lst[i][j]))
dx = [-1,0,1,0]
dy = [0,-1,0,1]
for i in range(4**len(cctv)):
    li = []
    for _ in range(len(cctv)):
        a = i%4
        li.append(a)
        i //= 4
    direction.append(li)
def check():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not arr[i][j]:
                cnt += 1
    return cnt
def see(x,y,d):
    nx = x
    ny = y
    while 1:
        nx += dx[d]
        ny += dy[d]
        if nx<0 or nx>=n or ny<0 or ny>=m or arr[nx][ny] == 6:
            return
        if not arr[nx][ny]:
            arr[nx][ny] = 1
for i in direction:
    arr = copy.deepcopy(lst)
    for j in range(len(i)):
        if cctv[j][2] == 1:
            see(cctv[j][0],cctv[j][1],i[j])
        elif cctv[j][2] == 2:
            see(cctv[j][0],cctv[j][1],i[j])
            see(cctv[j][0], cctv[j][1], (i[j]+2)%4)
        elif cctv[j][2] == 3:
            see(cctv[j][0],cctv[j][1],i[j])
            see(cctv[j][0], cctv[j][1], (i[j]+1)%4)
        elif cctv[j][2] == 4:
            see(cctv[j][0],cctv[j][1],i[j])
            see(cctv[j][0], cctv[j][1], (i[j]+1)%4)
            see(cctv[j][0], cctv[j][1], (i[j]+2)%4)
        elif cctv[j][2] == 5:
            see(cctv[j][0],cctv[j][1],i[j])
            see(cctv[j][0], cctv[j][1], (i[j]+1)%4)
            see(cctv[j][0], cctv[j][1], (i[j]+2)%4)
            see(cctv[j][0], cctv[j][1], (i[j] + 3) % 4)
    a = check()
    if a<result:
        result = a
print(result)
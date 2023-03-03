n, m, k = map(int, input().split())
arr = [list(map(int , input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
st = en = 0
result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == -1:
            if not st:
                st = i
            else:
                en = i
def clean():
    # arr[st-1][0] = 0
    arr[st][1] = 0
    # arr[en+1][0] = 0
    arr[en][1] = 0
def mise(x,y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m or arr[nx][ny] == -1:
            continue
        else:
            dust.append((nx,ny,arr[x][y]//5))
            cnt += 1
    arr[x][y] = arr[x][y] - (arr[x][y]//5) * cnt
def diffusion():
    for i in range(n):
        for j in range(m):
            if arr[i][j] != -1 and arr[i][j] != 0:
                mise(i,j)
    for x,y,z in dust:
        arr[x][y] += z
def aircon(st,en):
    ori = arr[st][1]
    i = 1
    key = 1
    up_key = 0
    ori_st, ori_en = st, en
    while 1:
        i += key
        st += up_key
        if i == m-1 and st:
            up_key = -1
            key = 0
        elif i == m-1 and not st:
            key = -1
            up_key = 0
        elif i == 0 and st == 0:
            key = 0
            up_key = 1
        if i==0 and st == ori_st :

            break
        ori, arr[st][i] = arr[st][i], ori

    ori = arr[en][1]
    i = 1
    key = 1
    up_key = 0
    while 1:
        i += key
        en += up_key
        if i == m-1 and en<n-1:
            up_key = 1
            key = 0
        elif i == m-1 and en == n-1:
            key = -1
            up_key = 0
        elif i == 0 and en == n-1:
            key = 0
            up_key = -1
        if i == 0 and en == ori_en:

            break
        ori, arr[en][i] = arr[en][i], ori
for _ in range(k):
    dust = []
    diffusion()
    aircon(st,en)
    clean()
for i in arr:
    result += sum(i)
print(result+2)
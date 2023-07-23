dxy = [(0,0),(1,0),(0,1),(1,1)]
arr = []
n = m = 0
erase = []
def inRange(x,y,cnt):
    if x<0 or x>=m or y<0 or y>=n or arr[x][y] != cnt:
        return False
    return True

def bfs(x,y):
    global arr,erase
    if not arr[x][y]: return
    for i,j in dxy:
        nx = x + i
        ny = y + j
        if not inRange(nx,ny,arr[x][y]): return
    erase.append((x,y))
    return

def goDown():
    for i in range(n):
        for j in range(m-1,0,-1):
            if arr[j][i]: continue
            for k in range(j-1,-1,-1):
                if arr[k][i]:
                    arr[j][i], arr[k][i] = arr[k][i], arr[j][i]
                    break
                
def solution(nm, nn, board):
    global arr, m, n, erase
    m = nm
    n = nn
    arr = []
    for i in range(m):
        arr.append(list(board[i]))

    for _ in range(300):
        erase = []
        for i in range(m):
            for j in range(n):
                bfs(i,j)
        for x,y in erase:
            for q,w in dxy:
                arr[x+q][y+w] = 0
        goDown()
    answer = 0
    for i in range(m):
        for j in range(n):
            if not arr[i][j]: answer += 1
    
    return answer
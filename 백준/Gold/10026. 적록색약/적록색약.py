import sys
sys.setrecursionlimit(3000) #재귀깊이 설정
input = sys.stdin.readline
n = int(input())
arr = []
count = 0
for _ in range(n):
    li = str(input().rstrip())
    arr.append(li)

arr_normal = []
for i in arr: #r,g,b를 숫자로 변경하는 과정
    li = []
    for j in i:
        if j=='R':
            li.append(0)
        elif j=='B':
            li.append(1)
        else:
            li.append(2)
    arr_normal.append(li)
arr_abnormal = []
for i in arr: #적록색약인 경우 r,g를 같은거로 봄
    li = []
    for j in i:
        if j=='B':
            li.append(0)
        else:
            li.append(1)
    arr_abnormal.append(li)

def dfs(x,y,rgb):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if arr_normal[x][y] == rgb:
        arr_normal[x][y] = 4 #탐색한 경우 방문표시를 위해 아예다른 숫자로 설정
        dfs(x-1,y,rgb)
        dfs(x+1,y,rgb)
        dfs(x,y+1,rgb)
        dfs(x,y-1,rgb)
        return True
for i in range(3): #경우가 r,g,b 3개이므로 3으로 설정 
    for k in range(n):
        for j in range(n): # 모든 구역에 대해 dfs실시
            if dfs(k,j,i) == True: #만약 한 구역 탐색이 끝날 시 구역 1회 증가
                count +=1
print(count, end=' ')
def dfs_ab(x,y,rgb): #정상 dfs와 같으나 리스트가 달라서 다시 설정
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if arr_abnormal[x][y] == rgb:
        arr_abnormal[x][y] = 4
        dfs_ab(x-1,y,rgb)
        dfs_ab(x+1,y,rgb)
        dfs_ab(x,y+1,rgb)
        dfs_ab(x,y-1,rgb)
        return True

count = 0
for i in range(2): #r,b 2개 탐색
    for k in range(n):
        for j in range(n):
            if dfs_ab(k,j,i) == True:
                count +=1
print(count)

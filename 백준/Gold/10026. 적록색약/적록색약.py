import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n = int(input())
arr = []
count = 0
for _ in range(n):
    li = str(input().rstrip())
    arr.append(li)

arr_normal = []
for i in arr:
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
for i in arr:
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
        arr_normal[x][y] = 4
        dfs(x-1,y,rgb)
        dfs(x+1,y,rgb)
        dfs(x,y+1,rgb)
        dfs(x,y-1,rgb)
        return True
for i in range(3):
    for k in range(n):
        for j in range(n):
            if dfs(k,j,i) == True:
                count +=1
print(count, end=' ')
def dfs_ab(x,y,rgb):
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
for i in range(2):
    for k in range(n):
        for j in range(n):
            if dfs_ab(k,j,i) == True:
                count +=1
print(count)

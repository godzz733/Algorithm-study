import sys
from collections import deque
input = sys.stdin.readline
t = int(input().rstrip())
arr = []
for i in range(t):
    li = str(input().rstrip())
    arr.append(list(map(int,li)))
count = 0
num = 0
li = []
def dfs(x,y):
    global count
    if x<0 or x>=t or y<0 or y>=t:
        return False
    if arr[x][y]==1:
        arr[x][y]=0
        count +=1
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x+1,y)
        dfs(x,y-1)
        return True
    return False

for i in range(t):
    for j in range(t):
        if dfs(i,j)==True:
            num +=1
            li.append(count)
            count = 0
li.sort()
print(num)
for i in li:
    print(i)
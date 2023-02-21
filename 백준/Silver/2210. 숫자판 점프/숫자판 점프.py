arr = [list(map(str, input().split())) for _ in range(5)]
visited = [[False] * 5 for _ in range(5)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = set()
lst= []
cnt = 0
def dfs(x,y):
    global lst, result, cnt
    if len(lst) == 6:
        if ''.join(lst) not in result:
            result.add(''.join(lst))
            cnt += 1
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or nx>=5 or ny<0 or ny>=5:
            continue
        lst.append(arr[nx][ny])
        dfs(nx,ny)
        lst.pop()
for i in range(5):
    for j in range(5):
        dfs(i,j)
print(cnt)

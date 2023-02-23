from collections import deque
n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = []
fire = set()
visited = set()
for i in range(n):
    lst = str(input())
    for k in range(m):
        if lst[k] == 'J':
            arr[i][k] = 1 # 시작위치
            man = (i,k,0)
            visited.add((i,k))
        elif lst[k] == 'F':
            arr[i][k] = 2 # 불
            visited.add((i,k))
            fire.add((i,k))
        elif lst[k] == '#':
            arr[i][k] = 3 # 벽
            key = 0
q = deque()
lst = set()
lst.add(man)
while lst:
    q.extend(lst)
    lst.clear()
    while q:
        x, y, cnt = q.popleft()
        if arr[x][y] != 1:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                result.append(cnt+1)
                break
            if arr[nx][ny] or (nx,ny) in visited:
                continue
            elif not arr[nx][ny] and (nx,ny) not in visited:
                arr[nx][ny] = 1
                lst.add((nx,ny,cnt + 1))
                visited.add((nx,ny))
    q.extend(fire)
    fire.clear()
    while q:
        x, y= q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if not arr[nx][ny]:
                arr[nx][ny] = 2
                fire.add((nx,ny))
            elif arr[nx][ny] == 1:
                arr[nx][ny] = 2
                fire.add((nx,ny))

if result:
    print(min(result))
else:
    print('IMPOSSIBLE')
from collections import deque
#
n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
for i in range(n): # 여긴 내가 편하려고 숫자로 바꿈, 굳이 안해도 됨
    for j in range(m):
        if arr[i][j] == 'W':
            arr[i][j] = 0
        else:
            arr[i][j] = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y,cnt):
    if not arr[x][y]: #만약 0인경우는 아예 방문을 안해서 시간을 줄임
        return 0
    _max = -1 # 이번 bfs에서 가장 큰 최소거리 = 답 을 구하기 위해 설정
    queue = deque([(x,y,cnt)]) #cnt로 가장 큰 최소거리를 나타낼거임
    visited[x][y] = True
    while queue:
        x, y, cnt = queue.popleft()
        if _max<cnt: #만약 현재 위치까지의 거리가 최대거리라면 _max에 값을 저장
            _max = cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if arr[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny,cnt+1)) # bfs를 돌고있는 현재 위치에서 시간 1을 추가해서 그 다음 위치로 넘어감
    return _max # 가장 큰 최소거리를 반환
result = 0
for i in range(n):
    for j in range(m):
        visited = [[False] * m for _ in range(n)]
        result = max(result, bfs(i,j,0)) #그중에서도 모든 그래프에 대해서 가장 큰 값을 저장
print(result)

from collections import deque
dx = [-1,0,0,1] # 위쪽으로 먼저가고 그다음 왼쪽으로 가야되서 방향 설정
dy = [0,-1,1,0]
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = 0
def bfs(x,y,cnt):
    global result
    q = deque()
    q.append((x,y,cnt))
    baby = 2 #상어크기
    feed = 0 #물고기 먹은 횟수
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    lst = [] # 같은 거리의 물고기 중 더 위에있고 더 왼쪽에 있는걸 찾을거임
    arr[x][y] = 0

    while 1:
        stop = 0 # 물고기를 먹을 수 있다면 1로 바뀔거임
        while q:
            x, y, cnt = q.popleft() # cnt는 이동 횟수
            for i in range(4):
                nx = x + dx[i]
                ny = y +dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue
                if not visited[nx][ny]:
                    if 0<arr[nx][ny]<baby: # 만약 먹을 수 있다면
                        visited[nx][ny] = True
                        if not lst:
                            lst.append((nx,ny,cnt+1)) # 먹을 수 있는 물고기 리스트에 넣음
                        else:
                            if cnt+1 <= lst[0][2]:
                                lst.append((nx,ny,cnt+1)) # 만약 먹을 순 있지만 거리가 멀다면 안넣음
                    elif arr[nx][ny]<=baby: # 먹진 못하고 지나갈 수만 있다면
                        visited[nx][ny] = True
                        q.append((nx,ny,cnt+1)) # 횟수만 증가시키고 다시 q에 넣음
        if lst:
            lst.sort(key=lambda x:(x[0],x[1])) # 먹을 수 있고 가장 짧은 거리에 있는 물고기 리스트
            x, y, cnt = lst[0][0], lst[0][1], lst[0][2] # sort를 통해서 가장 위에있고 가장 왼쪽에 있는걸 찾음
            arr[x][y] = 0 # 먹은 물고기는 빈칸으로 바꿔줌
            result += cnt # 물고기를 먹기위해 움직인 횟수 체크
            stop = 1 # 물고기를 먹었기 때문에 1로 만듬
            feed += 1 # 물고기를 먹었기 때문에 먹은 수 +1
            lst.clear() # 이제 물고기 리스트는 비워줌
            q.append((x,y,0)) # 다음 시작점으로 쓰기위해 q에 추가
            visited = [[False] * n for _ in range(n)] # 다시 돌기위해 방문 초기화
        if feed == baby: # 만약 지금 크기와 같은 수의 먹이를 먹었다면
            baby += 1 # 크기 1증가
            feed = 0 # 먹은 물고기 수 초기화
        if not stop: # 만약 물고기를 못먹는다면
            return # 종료
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            bfs(i,j, 0)
print(result)

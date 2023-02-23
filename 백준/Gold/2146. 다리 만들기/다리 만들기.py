from collections import deque
n = int(input())
arr = [list(map(int ,input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

num = []
land = set() # 이미 탐색한 지역
def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited = set() # 현재 지역에서 현재 지역으로 다리를 건설할 경우를 제외
    water = set() # 물과 땅의 구역부터 다리가 시작하므로
    visited.add((x,y))
    water_visited = set() # 한번 지난 물을 다시 지나지 않기 위해
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if (nx,ny) not in visited:
                if arr[nx][ny]: # 현재 지역을 다 돌기위함
                    visited.add((nx,ny))
                    q.append((nx,ny))
                    land.add((nx,ny)) # 한번 순회한 지역을 다시 돌지 않기위해 저장장                elif not arr[nx][ny]:
                    water.add((x,y,0)) # 물과의 경계를 저장, x,y,라벨,이동횟수
    q.extend(water) # 이제 다리를 건설할거임
    while q:
        x, y, result = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not arr[nx][ny] and (nx,ny) not in water_visited: # 만약 물을 지나가는 거라면
                q.append((nx, ny,result + 1)) # 물 한칸을 지날때마다 다리 갯수 1씩 증가
                water_visited.add((nx,ny)) # 지나온 물을 다시 안지나가기 위함
            elif arr[nx][ny] and (nx,ny) not in visited: # 만약 다리를 건설하다가 새로운 땅을 만낫다면
                num.append(result) # 결과값에 저장
                return
for i in range(n):
    for j in range(n):
        if (i,j) not in land and arr[i][j]: # 한번도 안지나간 지역이고 땅이라면
            bfs(i,j)
print(min(num)) # 건설한 다리 중 최소값

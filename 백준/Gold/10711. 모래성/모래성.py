from collections import deque
n, m = map(int, input().split())
arr = []
water = deque() # 모래성이 없는 곳을 저장할거임
result = 0
visited = [[0] * m for _ in range(n)]
for i in range(n):
    lst = list(str(input()))
    for j in range(m):
        if not lst[j].isdigit():
            lst[j] = 0
            water.append((i,j)) # 모래성이 없다면 저장
        else:
            lst[j] = int(lst[j])
    arr.append(lst)
dxy = [(1,1),(1,-1),(-1,1),(-1,-1),(1,0),(-1,0),(0,-1),(0,1)] # 델타
while water:
    x,y = water.popleft()
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if nx <0 or nx>=n or ny<0 or ny>=m:
            continue
        if arr[nx][ny]: # 만약 파도가 치는데 옆이 모래성이라면
            arr[nx][ny] -= 1 # -1을 해주는데 이때 이 모래성이 부서질 수 없다면 어처피 0이 되지 않으므로 상관없음
            if not arr[nx][ny]: # 만약 0이됫다면
                visited[nx][ny] = visited[x][y] + 1 # 방문 횟수를 1 증가시켜 결과값을 구할 때 사용할거임
                result = max(result,visited[nx][ny]) # 결과값에 1 증가
                water.append((nx,ny)) # 모래성이 하나 없어졋다면 그 다음에는 물로 사용되므로 추가함
print(result)
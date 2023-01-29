#방문하지 않고 바로 전에 방문햇던 노드에서 가장 가까운 노드 중 거리가 짧은 노드의 인덱스를 반환한다.
def now(arr_leng, visited): 
        _min = int(1e9)
        x = -1
        y = -1
        for i in range(n):
            for k in range(n):
                if arr_leng[i][k]<_min and not visited[i][k]:
                    _min = arr_leng[i][k]
                    x = i
                    y = k
        return (x,y)

t = int(input())
for test_case in range(1,t+1):
    n = int(input())
    INF = int(1e9)
    visited = [[False for _ in range(n)] for _ in range(n)]
    arr = []
    arr_leng = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        arr.append(list(map(int, input())))
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    arr_leng[0][0] = 0
    current_node = (0,0) #스타트 노드 설정
    while 1:
        current_node = now(arr_leng, visited) #현재 방문하지 않앗고 바로 방문한 직전 노드에서 가장 가까운 노드의 인덱스를 받아옴, 맨 처음엔 스타트 노드인 0,0이 반환될것임
        x = current_node[0]
        y = current_node[1]
        if x==-1 and y==-1: #만약 모든 노드를 방문하여 now함수에서 -1,-1을 반환한다면 반복문을 끝냄
            break
        for i in range(4): #현재 노드를 기준으로 상,하,좌,우를 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n: #범위를 벗어난다면 중지
                continue
            if arr_leng[nx][ny] > arr_leng[x][y] + arr[nx][ny]: #만약 이미 저장되있던 거리보다 현재 노드를 거쳐 가는게 더 빠르다면 그 거리를 저장한다.
                arr_leng[nx][ny] = arr_leng[x][y] + arr[nx][ny]
        visited[x][y] = True #현재 방문을 마친 노드를 방문처리 함

    print(f'#{test_case} {arr_leng[n-1][n-1]}')

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
    current_node = (0,0)
    while 1:
        current_node = now(arr_leng, visited)
        x = current_node[0]
        y = current_node[1]
        if x==-1 and y==-1:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if arr_leng[nx][ny] > arr_leng[x][y] + arr[nx][ny]:
                arr_leng[nx][ny] = arr_leng[x][y] + arr[nx][ny]
        visited[x][y] = True

    print(f'#{test_case} {arr_leng[n-1][n-1]}')

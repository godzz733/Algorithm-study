from collections import deque
def solution(land):
    answer = 0
    q = deque()
    arr = [[0] * len(land[0]) for _ in range(len(land))]
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    idx = 1
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j]:
                lst = set()
                lst.add((i,j))
                q.append((i,j))
                land[i][j] = 0
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<len(land) and 0<=ny<len(land[0]) and land[nx][ny]:
                            lst.add((nx,ny))
                            q.append((nx,ny))
                            land[nx][ny] = 0
                for x,y in lst:
                    arr[x][y] = (idx,len(lst))
                idx += 1
    # for i in range(len(arr)):
    #     for j in range(len(arr[0])):
    #         print(arr[i][j], end=' ')
    #     print()
    
    for i in range(len(land[0])):
        lst = set()
        tem = 0
        for j in range(len(land)):
            if arr[j][i] and arr[j][i][0] not in lst:
                lst.add(arr[j][i][0])
                tem += arr[j][i][1]
        answer = max(tem,answer)
        
            
    return answer
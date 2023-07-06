from collections import deque
for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(2)]
    q = deque()
    q.append((0,0,arr[0][0],1))
    q.append((1,0,arr[1][0],1))
    visited = [[[0] * n for _ in range(2)] for i in range(2)] 
    # visited[1][0][0] = arr[0][0]
    # visited[1][1][0] = arr[1][0]
    result = 0
    while q:
        x,y,cnt,key = q.popleft()
        result = max(result,cnt)
        if y == n-1 or visited[key][x][y] > cnt: continue
        if not key:
            if visited[key][0][y+1] < cnt+arr[0][y+1]:
                q.append((0,y+1,cnt+arr[0][y+1],1))
                visited[key][0][y+1] = cnt+arr[0][y+1]
            if visited[key][1][y+1] < cnt+arr[1][y+1]:
                q.append((1,y+1,cnt+arr[1][y+1],1))
                visited[key][1][y+1] = cnt+arr[1][y+1]
        else:
            if visited[key][0][y+1] < cnt:
                q.append((0,y+1,cnt,0))
                visited[key][0][y+1] = cnt
            if visited[key][1][y+1] < cnt:
                q.append((1,y+1,cnt,0))
                visited[key][1][y+1] = cnt
            if x == 0:
                if visited[key][1][y+1] < cnt+arr[1][y+1]:
                    q.append((1,y+1,cnt+arr[1][y+1],1))
                    visited[key][1][y+1] = cnt+arr[1][y+1]
            else:
                if visited[key][0][y+1] < cnt+arr[0][y+1]:
                    q.append((0,y+1,cnt+arr[0][y+1],1))
                    visited[key][0][y+1] = cnt+arr[0][y+1]
    print(result )

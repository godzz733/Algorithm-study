from collections import deque
def solution(maze):
    answer = 0
    q = deque()
    x1,x2,y1,y2 = 0,0,0,0
    n,m = len(maze), len(maze[0])
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                x1,y1 = i,j
            elif maze[i][j] == 2:
                x2,y2 = i,j
    q.append((x1,y1,x2,y2,1<<(x1*n+y1),1<<(x2*n+y2),0))
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while q:
        x1,y1,x2,y2,d1,d2,cnt = q.popleft()
        if maze[x1][y1] == 3 and maze[x2][y2] == 4:
            return cnt
        for i in range(4):
            for j in range(4):
                nx1 = x1 + dx[i]
                ny1 = y1 + dy[i]
                nx2 = x2 + dx[j]
                ny2 = y2 + dy[j]
                if maze[x1][y1] == 3:
                    if (x1,y1) != (nx2,ny2) and 0<=nx2<n and 0<=ny2<m and (x1,y1) != (nx2,ny2) and maze[nx2][ny2] != 5 and not d2&(1<<(nx2*n+ny2)):
                        q.append((x1,y1,nx2,ny2,0,d2|(1<<(nx2*n+ny2)),cnt+1))
                elif maze[x2][y2] == 4:
                    if (x2,y2) != (nx1,ny1) and 0<=nx1<n and 0<=ny1<m and (x2,y2) != (nx1,ny1) and maze[nx1][ny1] != 5 and not d1&(1<<(nx1*n+ny1)):
                        q.append((nx1,ny1,x2,y2,d1|(1<<(nx1*n+ny1)),0,cnt+1))
                else:

                    if not ((x1,y1) == (nx2,ny2) and (x2,y2) == (nx1,ny1)) and 0<=nx1<n and 0<=ny1<m and 0<=nx2<n and 0<=ny2<m and (nx1,ny1) != (nx2,ny2) and maze[nx1][ny1] != 5 and maze[nx2][ny2] != 5 and not d1&(1<<(nx1*n+ny1)) and not d2&(1<<(nx2*n+ny2)):
                        q.append((nx1,ny1,nx2,ny2,d1|(1<<(nx1*n+ny1)),d2|(1<<(nx2*n+ny2)),cnt+1))
    return answer
from collections import deque
def solution(n, m, x, y, r, c, k):
    answer = ''
    dx = [1,0,0,-1]
    dy = [0,-1,1,0]
    dz = ['d','l','r','u']
    q = deque()
    q.append((x,y,0,""))
    while q:
        x,y,cnt,d = q.popleft()
        if (x,y) == (r,c) and cnt == k:
            return d
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<=0 or nx>n or ny<=0 or ny>m: continue
            if abs(nx - r) + abs(ny - c) + cnt + 1 > k:continue
            q.append((nx,ny,cnt+1,d+dz[i]))
            break
    return "impossible"
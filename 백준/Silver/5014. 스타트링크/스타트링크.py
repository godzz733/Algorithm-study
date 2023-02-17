from collections import deque
f,s,g,u,d = map(int,input().split()) #f=최고층, g = 도착, s=현재위치, u=위로 d=아래로 (없으면 안감)
visited= set()
def up(x):
    x += u
    return x
def down(x):
    x -= d
    return x
dx = [up,down]
def bfs(x,cnt):
    q = deque()
    q.append((x,cnt))
    visited.add(x)
    if x == g:
        return cnt - 1
    while q:
        x,cnt = q.popleft()
        for i in range(2):
            nx = dx[i](x)
            if 1<=nx<=f:
                if nx == g:
                    return cnt
                if nx not in visited:
                    visited.add(nx)
                    q.append((nx,cnt+1))
a = bfs(s,1)
print(a) if a != None else print('use the stairs')
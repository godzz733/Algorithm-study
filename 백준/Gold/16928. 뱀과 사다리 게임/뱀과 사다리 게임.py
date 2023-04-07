from collections import deque
n,m = map(int,input().split())
ladder = [0] * 101
snake = [0] * 101
visited = [1000000] * 101
result = 1000000
for _ in range(n):
    a, b = map(int,input().split())
    ladder[a] = b
for _ in range(m):
    a, b = map(int,input().split())
    snake[a] = b
q = deque()
q.append((1,0))
visited[1] = 0
while q:
    x, cnt = q.popleft()
    if x == 100:
        result = cnt
        break
    for i in range(1,7):
        nx = x + i
        if nx>100 or cnt+1 >= visited[nx]:
            continue
        if not ladder[nx] and not snake[nx]:
            q.append((nx,cnt+1))
            visited[nx] = cnt+1
        elif ladder[nx]:
            q.append((ladder[nx],cnt+1))
            visited[ladder[nx]] = cnt+1
        else:
            q.append((snake[nx],cnt+1))
            visited[snake[nx]] = cnt+1
print(result)
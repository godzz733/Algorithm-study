from collections import deque
n, m = map(int,input().split())

def bfs(n, num):
    queue = deque()
    queue.append((n,num))
    while queue:
        x, num= queue.popleft()
        if x == m:
            return num
        if x<m:
            queue.append((x*2, num+1))
            queue.append((x*10+1,num+1))
    return -1
print(bfs(n,1))
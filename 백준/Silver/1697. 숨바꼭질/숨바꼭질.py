import sys
from collections import deque

start, end = map(int, sys.stdin.readline().rstrip().split())
visited = [False] * 200001
time = [0] * 200001


def bfs(start):
    queue = deque()
    queue.append(start)
    depth = []
    cnt = 0
    while not visited[end]:
        queue.extend(depth)
        depth.clear()
        cnt += 1
        while queue:
            v = queue.popleft()
            if v < 0 or v > 100000:
                pass
            else:
                if not visited[v - 1]:
                    depth.append(v-1)
                    time[v-1] = cnt
                    visited[v-1] = True
                if not visited[v+1]:
                    depth.append(v+1)
                    time[v + 1] = cnt
                    visited[v+1] = True
                if not visited[v*2]:
                    depth.append(v*2)
                    time[v*2] = cnt
                    visited[v*2] = True



bfs(start)
if start==end:
    print(0)
else:
    print(time[end])
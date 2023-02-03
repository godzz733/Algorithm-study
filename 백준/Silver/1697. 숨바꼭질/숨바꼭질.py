import sys
from collections import deque

start, end = map(int, sys.stdin.readline().rstrip().split())
visited = [False] * 200001 # 방문 설정
time = [0] * 200001 # 몇 초가 걸렷는지?


def bfs(start):
    queue = deque()
    queue.append(start) # 일단 시작지점을 큐에 넣음
    depth = [] # 한 계층씩 실행하기 위해 새로 리스트를 넣음
    cnt = 0 # 몇 초가 걸렷는지
    while not visited[end]:
        queue.extend(depth) # 한 계층 씩 큐에 넣을거임
        depth.clear() # 넣었으면 초기화
        cnt += 1 # 1초씩 증가
        while queue:
            v = queue.popleft() #bfs 실행
            if v < 0 or v > 100000:
                pass
            else: # 방문하지 않았을때만 실행
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
if start==end: # 시작과 도착이 같을 때는 0
    print(0)
else:
    print(time[end])

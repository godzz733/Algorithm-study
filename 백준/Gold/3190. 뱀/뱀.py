import sys; input = sys.stdin.readline
from collections import deque
# N <= 100, K <= 100, X <= 10000, 'L' = 왼쪽 90도, 'D' = 오른쪽 90도
# 최대 만초에 1초당 머리, 꼬리 두개만 이동하므로 충분히 완전탐색 가능
# 몸은 2, 사과는 1로 설정
n = int(input())
arr = [[0]*n for _ in range(n)]
for _ in range(int(input())):
    a,b = map(int,input().split())
    arr[a-1][b-1] = 1
dxy = [(0,1),(1,0),(0,-1),(-1,0)]
d = 0
arr[0][0] = 2
head = [0,0]
tails = deque()
tails.append([0,0])
ans = 0
time = {}
for _ in range(int(input())):
    X,C = map(str,input().rstrip().split())
    time[int(X)] = 1 if C == 'D' else -1

while 1:
    ans += 1
    head[0] += dxy[d][0]
    head[1] += dxy[d][1]
    tails.append(head[::])
    if head[0] < 0 or head[0] >=n or head[1] < 0 or head[1] >= n or arr[head[0]][head[1]] == 2:
        print(ans)
        break
    if arr[head[0]][head[1]] == 1:
        arr[head[0]][head[1]] = 2
    else:
        tail = tails.popleft()
        arr[tail[0]][tail[1]] = 0
        arr[head[0]][head[1]] = 2
    if ans in time:
        d = (d+time[ans]) % 4 if (d+time[ans]) >= 0 else 4+(d+time[ans])

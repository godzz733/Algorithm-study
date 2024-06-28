import sys; input = sys.stdin.readline
from collections import deque
n = int(input())
q = deque()
idx = 1
for _ in range(n):
    arr = list(map(str,input().rstrip().split()))
    if arr[0] == 'D':
        if arr[1] == 'R':
            for i in range(int(arr[2])):
                q.pop()
        else:
            for i in range(int(arr[2])):
                q.popleft()
    elif arr[1] == 'L':
        q.appendleft(idx)
        idx += 1
    else:
        q.append(idx)
        idx += 1
while q:
    print(q.popleft())
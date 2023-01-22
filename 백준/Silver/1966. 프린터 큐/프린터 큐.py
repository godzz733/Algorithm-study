import sys
from collections import deque
t = int(input())
for i in range(t):
    n,m = map(int, sys.stdin.readline().split())
    arr = [*map(int, sys.stdin.readline().split())]
    queue = deque(arr)
    count = 0
    witch = m
    num = 0
    while arr[m]!=max(queue):
        if queue[0]<max(queue):
            a = queue.popleft()
            queue.append(a)
            witch -=1
            if witch<0:
                witch=len(queue)-1
        elif queue[0]==max(queue):
            queue.popleft()
            num+=1
            witch -=1
            if witch<0:
                witch=len(queue)-1
    for k in range(0,witch):
        if queue[k]==arr[m]:
            num += 1
    
    print(num+1)
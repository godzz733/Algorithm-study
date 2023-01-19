import sys
n = int(input())
deque = []
for _ in range(n):
    arr = [*map(str, sys.stdin.readline().split())]
    if arr[0]=='push':
        deque.insert(0,arr[1])
    elif arr[0]=='pop':
        if deque==[]:
            print(-1)
        else:
            print(deque.pop())
    elif arr[0]=='size':
        print(len(deque))
    elif arr[0]=='empty':
        if deque==[]:
            print(1)
        else:
            print(0)
    elif arr[0]=='front':
        if deque==[]:
            print(-1)
        else:
            print(deque[-1])
    elif arr[0]=='back':
        if deque==[]:
            print(-1)
        else:
            print(deque[0])
import sys
t = int(input())
result = []
for i in range(t):
    stack = [*map(str , sys.stdin.readline().split())]
    if stack[0] == 'push':
        result.append(int(stack[1]))
    elif stack[0] == 'top':
        if result==[]:
            print(-1)
        else:
            print(result[-1])
    elif stack[0] == 'size':
        print(len(result))
    elif stack[0] == 'empty':
        if result==[]:
            print(1)
        else:
            print(0)
    elif stack[0] =='pop':
        if result==[]:
            print(-1)
        else:
            print(result.pop())


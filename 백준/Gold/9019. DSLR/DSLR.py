from collections import deque
t = int(input())
def D(x,y):
    x = int(x)*2
    y += 'D'
    return x%10000, y
def S(x,y):
    x = int(x) - 1
    y += 'S'
    if x == -1:
        return 9999, y
    else:
        return x, y
def L(x,y):
    front = x%1000
    back = x//1000
    y += 'L'
    return front*10 + back, y
def R(x,y):
    front = x%10
    back = x//10
    y += 'R'
    return front*1000 + back, y

for _ in range(t):
    a, b = map(int, input().split())
    visited = set()
    DSLR = [D,S,L,R]

    def bfs(a):
        q = deque()
        q.append([a,''])
        while q:
            x, y = q.popleft()
            for i in range(4):
                result_x, result_y = DSLR[i](x,y)
                if result_x == b:
                    return result_x, result_y
                if result_x not in visited:
                    visited.add(result_x)
                    q.append((result_x, result_y))
    print(bfs(a)[1])
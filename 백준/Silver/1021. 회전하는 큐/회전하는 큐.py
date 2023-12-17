import sys;input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
lst = list(map(int,input().split()))
arr = [i for i in range(1,n+1)]
ans = 0
def left(x):
    q = deque(arr)
    num = 0
    while q[0] != x:
        q.append(q.popleft())
        num += 1
    return num, q

def right(x):
    q = deque(arr)
    num = 0
    while q[0] != x:
        q.appendleft(q.pop())
        num += 1
    return num, q
for i in lst:
    l , r = left(i), right(i)
    if l[0] > r[0]:
        ans += r[0]
        arr = r[1]
    else:
        ans += l[0]
        arr = l[1]
    arr.popleft()
print(ans)
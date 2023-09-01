from collections import deque
q = deque([i for i in range(1,int(input())+1)])
ans = []
size = len(q)
for i in range(size-1):
    ans.append(q.popleft())
    q.append(q.popleft())
print(*(ans+list(q)))
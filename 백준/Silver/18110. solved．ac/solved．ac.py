from collections import deque
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()
q= deque()
q.extend(arr)
x = round(len(q)*0.15 + 0.0000001)
for i in range(x):
    q.popleft()
    q.pop()
if not n:
    print(0)
else:   
    print(round((sum(q)/len(q)) + 0.0000001))
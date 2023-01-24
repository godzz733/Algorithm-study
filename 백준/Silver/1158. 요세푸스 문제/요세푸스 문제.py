from collections import deque

a, b = map(int ,input().split())
arr = [x for x in range(1,a+1)]
queue = deque(arr)
result = []
while len(queue)!=0:
    queue.rotate(-b)
    q = queue.pop()
    result.append(q)

print('<',end='')
for i in range(a-1):
    print(result[i],end=', ')
print(result[-1],end='')
print('>')
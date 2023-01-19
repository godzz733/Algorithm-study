from collections import deque
a = int(input())

arr = deque([i for i in range(1,a+1)])
while len(arr)>2:
    arr.popleft()
    arr.append(arr[0])
    arr.popleft()
if len(arr) <2:
    print(arr[0])
else:
    print(list(arr)[1])

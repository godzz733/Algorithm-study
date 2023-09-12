from collections import deque
n = int(input())
arr = [int(input()) for _ in range(n)]
stack = deque()
ans = 0
for i in range(n-1):
    if arr[i] > arr[i+1]:
        stack.append((arr[i],i))
    else:
        while stack:
            tem = stack.pop()
            if tem[0] <= arr[i+1]:
                ans += (i-tem[1])
            else:
                stack.append(tem)
                break
while stack:
    tem = stack.popleft()
    ans += (n-1-tem[1])
print(ans)
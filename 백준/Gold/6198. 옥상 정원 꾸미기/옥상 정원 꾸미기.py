n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
ans = 0
for i in arr:
    while stack and stack[-1] <= i:
        stack.pop()
    stack.append(i)
    ans += len(stack) - 1
print(ans)
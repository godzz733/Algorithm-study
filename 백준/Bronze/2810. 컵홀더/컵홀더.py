n = int(input())
lst = list(str(input()))
stack = []
result = 0
for i in lst:
    if i == 'S':
        if not stack:
            stack.append('*')
            stack.append('S')
            stack.append('*')
        elif stack[-1] == '*':
            stack.append('S')
            stack.append('*')
    else:
        if not stack:
            stack.append('*')
            stack.append('L')
        elif stack[-1] == 'L':
            stack.append('L')
            stack.append('*')
        elif stack[-1] == '*':
            stack.append('L')
if stack.count('*') >= n:
    print(n)
else:
    print(stack.count('*'))
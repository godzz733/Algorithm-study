tokens = list(map(str, input().rstrip()))
lst = []
stack = []
prior = {'*': 3,'/':3, '+': 2,'-':2, '(': 1}
for n in range(len(tokens)):
    if tokens[n].isalpha():
        lst.append(tokens[n])
    elif tokens[n] == '(':
        stack.append(tokens[n])
    elif tokens[n] == ')':
        while stack[-1] != '(':
            lst.append(stack.pop())
        stack.pop()
    else:
        while stack and prior[tokens[n]] <= prior[stack[-1]]:
            lst.append(stack.pop())
        stack.append(tokens[n])

while len(stack) != 0:
    lst.append(stack.pop())

print(''.join(lst))
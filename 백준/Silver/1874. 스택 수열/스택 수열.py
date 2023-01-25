t = int(input())
arr = [x for x in range(t,0,-1)]
inp_arr = []
stack = []
result = []
for i in range(t):
    a = int(input())
    inp_arr.append(a)
key = 0
for i in range(t):
    if stack==[]:
        c = arr.pop()
        stack.append(c)
        result.append('+')
        while inp_arr[i]!=stack[-1]:
            b =arr.pop()
            stack.append(b)
            result.append('+')
    elif inp_arr[i]!=stack[-1] and inp_arr[i]>stack[-1]:
        while inp_arr[i]!=stack[-1]:
            b =arr.pop()
            stack.append(b)
            result.append('+')
    elif inp_arr[i]!=stack[-1] and inp_arr[i]<stack[-1]:
        key +=1
        break
    if inp_arr[i]==stack[-1]:
        d = stack.pop()
        result.append('-')

if key==0:
    [print(x) for x in result]
else:
    print('NO')
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
    if stack==[]: #스택이 비어있을 상황 생각
        c = arr.pop()
        stack.append(c)
        result.append('+')
        while inp_arr[i]!=stack[-1]: #현재 입력값 까지 stack에 넣음
            b =arr.pop()
            stack.append(b)
            result.append('+') #넣었으면 '+' 추가
    elif inp_arr[i]!=stack[-1] and inp_arr[i]>stack[-1]: #만약 지금 stack의 마지막 값이 inp_arr의 값보다 작다면 inp_arr 값까지 arr에서 pop해서 집어넣음
        while inp_arr[i]!=stack[-1]:
            b =arr.pop()
            stack.append(b)
            result.append('+')
    elif inp_arr[i]!=stack[-1] and inp_arr[i]<stack[-1]: #만약 stack의 마지막 값이 inp_arr보다 크면서 다르다? == 오류 -> key값을 +1해서 안된다는걸 표시
        key +=1
        break
    if inp_arr[i]==stack[-1]: #만약 stack의 마지막 값이 inp_arr와 같다면 pop하고 '-' 
        d = stack.pop()
        result.append('-')

if key==0:
    [print(x) for x in result]
else:
    print('NO')

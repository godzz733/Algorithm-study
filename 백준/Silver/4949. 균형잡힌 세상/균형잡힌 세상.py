import sys
input = sys.stdin.readline
while 1:
    key = 0
    word = list(str(input().rstrip()))
    if word == ['.']:
        break
    arr = []
    dic = {'(':0,'[':0}
    test = []
    for i in word:
        if i == '(' or i==')' or i=='[' or i==']':
            arr.append(i)
    try:
        for i in arr:
            if i =='(' or i=='[':
                test.append(i)
            else:
                a = test.pop()
                if i==']' and a=='(':
                    key +=1
                    break
                elif i==')' and a=='[':
                    key +=1
                    break
    except:
        key+=1
    if test!=[]:
        key+=1
    
    if not key:
        print('yes')
    else:
        print('no')
     
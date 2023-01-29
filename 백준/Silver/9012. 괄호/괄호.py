import sys
input = sys.stdin.readline
n = int(input().rstrip())
for _ in range(n):
    key = 0
    word = list(str(input().rstrip()))
    arr = []
    test = []
    for i in word:
        if i == '(' or i==')':
            arr.append(i)
    try:
        for i in arr:
            if i =='(':
                test.append(i)
            else:
                a = test.pop()
    except:
        key+=1
    if test!=[]:
        key+=1
    
    if not key:
        print('YES')
    else:
        print('NO')

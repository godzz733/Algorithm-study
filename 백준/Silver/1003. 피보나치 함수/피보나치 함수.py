t = int(input())

for i in range(t):
    d = [0,0]*41
    d[0] = [1,0]
    d[1] = [0,1]
    a = int(input())
    if a==0:
        print(' '.join(map(str,d[0])))
    elif a==1:
        print(' '.join(map(str,d[1])))
    else:
        for k in range(2,a+1):
            d[k]=[d[k-1][0]+d[k-2][0],d[k-1][1]+d[k-2][1]]
        print(' '.join(map(str,d[k])))


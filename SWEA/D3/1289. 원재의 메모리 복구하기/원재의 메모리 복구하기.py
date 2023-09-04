for tc in range(1,int(input())+1):
    a = input()
    idx = a.index('1')
    ans = 1
    for i in range(idx+1,len(a)):
        if a[i] != a[i-1]: ans +=1
    print(f'#{tc} {ans}')
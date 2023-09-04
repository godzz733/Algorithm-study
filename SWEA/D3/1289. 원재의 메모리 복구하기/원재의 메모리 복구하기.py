for tc in range(1,int(input())+1):
    a = input()
    ans = int(a[0])
    for i in range(1,len(a)):
        if a[i] != a[i-1]: ans +=1
    print(f'#{tc} {ans}')
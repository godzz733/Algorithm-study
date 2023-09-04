for tc in range(1,int(input())+1):
    a = input()
    ans = 0
    idx=  0
    while idx < len(a):
        if a[idx] == ')':
            ans += 1
            idx += 1
        elif a[idx] == '(':
            ans += 1
            if idx == len(a)-1:
                ans += 1
                break
            if a[idx+1] == ')':
                idx += 2
            else:
                idx += 1
        else: idx += 1
    print(f'#{tc} {ans}')
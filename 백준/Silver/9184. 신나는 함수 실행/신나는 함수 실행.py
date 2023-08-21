def recur(a,b,c):
    global dic
    if a<=0 or b<=0 or c<=0: return 1
    if a>20 or b>20 or c>20: return recur(20,20,20)
    if (a,b,c) in dic: return dic[(a,b,c)]
    if a<b and b<c:
        _a = recur(a,b,c-1)
        _b = recur(a,b-1,c-1)
        _c = recur(a,b-1,c)
        dic[(a,b,c-1)] = _a
        dic[(a,b-1,c-1)] = _b
        dic[(a,b-1,c)] = _c 
        tem = _a + _b - _c
        dic[(a,b,c)] = tem
        return tem
    else:
        _a = recur(a-1,b,c)
        _b = recur(a-1,b-1,c)
        _c = recur(a-1,b,c-1)
        _d = recur(a-1,b-1,c-1)
        dic[(a-1,b,c)] = _a
        dic[(a-1,b-1,c)] = _b
        dic[(a-1,b,c-1)] = _c
        dic[(a-1,b-1,c-1)] = _d
        tem = _a + _b + _c - _d
        dic[(a,b,c)] = tem
        return tem
dic = {}
while 1:
    a,b,c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:break
    ans = recur(a,b,c)
    print(f'w({a}, {b}, {c}) = {ans}')
    
n,m = map(int,input().split())
size = len(str(n))
nm = n%m
cnt = 1
_set = set()
while 1:
    # print(n%m)
    if n%m == 0: print(cnt); break
    if n%m in _set: print(-1); break
    _set.add(n%m)
    n = ((n%m * (10**size)) + nm) % m
    cnt += 1

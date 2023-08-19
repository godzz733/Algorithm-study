_set = set()
_set.add('ChongChong')
for _ in range(int(input())):
    a,b = map(str,input().split())
    if a in _set:
        _set.add(b)
    elif b in _set:
        _set.add(a)
print(len(_set))
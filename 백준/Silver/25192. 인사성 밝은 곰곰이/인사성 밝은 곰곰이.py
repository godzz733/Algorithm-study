n = int(input())
ans = 0
_set = set()
for _ in range(n):
    tem = input()
    if tem != 'ENTER' and tem not in _set:
        ans+=1
        _set.add(tem)
    elif tem == 'ENTER':_set.clear()
print(ans)
a = input()
b = input()
arr = set()
arr.add(b)
ans = 0
for _ in range(len(b) - len(a)):
    tem = []
    for j in arr:
        if j[-1] == 'A':
            tem.append(''.join(j[:-1]))
        if j[0] == 'B':
            tem.append(''.join(reversed(j[1:])))
    if a in tem:
        ans = 1
        break
    arr = set(tem)
print(ans)
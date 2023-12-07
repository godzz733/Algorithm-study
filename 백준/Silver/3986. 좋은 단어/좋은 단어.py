import sys;input = sys.stdin.readline
n = int(input())
ans = 0
for _ in range(n):
    arr = input().rstrip()
    if arr.count('A') & 1 or arr.count('B') & 1: continue
    tem = []
    for i in arr:
        if not tem: tem.append(i)
        elif tem[-1] == i: tem.pop()
        else: tem.append(i)
    tem = ''.join(tem)
    if 'ABA' in tem or 'BAB' in tem: continue
    ans += 1
print(ans)
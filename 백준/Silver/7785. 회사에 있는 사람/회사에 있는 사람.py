dic = {}
for _ in range(int(input())):
    a, b = map(str, input().split())
    if a not in dic and b == 'enter': dic[a] = 1
    elif a in dic and b == 'leave': dic.pop(a)
ans = []
for x,y in dic.items():
    ans.append(x)
ans.sort(reverse=True)
for i in ans: print(i)
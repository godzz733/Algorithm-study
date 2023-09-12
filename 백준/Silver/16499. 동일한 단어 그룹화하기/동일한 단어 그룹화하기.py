import sys;input = sys.stdin.readline
n = int(input())
_set = []
for _ in range(n):
    tem = list(input())
    dic = {}
    for i in tem:
        if i in dic:dic[i] += 1
        else:dic[i] = 1
    if not dic in _set:_set.append(dic)
print(len(_set))
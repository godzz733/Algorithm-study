import sys
def find_parent(x):
    if x != dic[x][0]:
        x = find_parent(dic[x][0])
    return dic[x][0]
def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a<b:
        dic[b][0] = a
        dic[a][1] += dic[b][1]
    else:
        dic[a][0] = b
        dic[b][1] += dic[a][1]
for _ in range(int(input())):
    n = int(input())
    dic = {}
    for _ in range(n):
        a,b = map(str,sys.stdin.readline().split())
        if a not in dic:
            dic[a] = [a,1]
        if b not in dic:
            dic[b] = [b,1]
        a = find_parent(a)
        b = find_parent(b)
        if a!=b:
            union_parent(a,b)
        print(dic[dic[find_parent(a)][0]][1])
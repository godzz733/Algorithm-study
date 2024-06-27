import sys; input = sys.stdin.readline
n = int(input())
dic = {}
for _ in range(n-1):
    a,b = map(str,input().rstrip().split())
    dic[a] = b
    if b not in dic:
        dic[b] = -1

a,b = map(str,input().rstrip().split())
_a,_b = a,b
while dic[_a] != -1:
    if dic[_a] == b:
        print(1)
        exit()
    _a = dic[_a]
while dic[_b] != -1:
    if dic[_b] == a:
        print(1)
        exit()
    _b = dic[_b]
print(0)
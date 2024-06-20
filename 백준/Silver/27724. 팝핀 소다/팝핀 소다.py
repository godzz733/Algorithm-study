import sys; input = sys.stdin.readline
n,m,k = map(int,input().split())
a,b = 0,0
for i in range(19):
    if n == 1<<i:
        a = i
        break
for i in range(19):
    if k < 1<<i:
        b = i - 1
        break
print(min(a,b+m))
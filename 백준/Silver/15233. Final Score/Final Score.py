import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
a = list(map(str,input().split()))
b = list(map(str,input().split()))
c = list(map(str,input().split()))
z,x = 0,0
for i in c:
    if i in a: z += 1
    else: x += 1
if z>x:print('A')
elif x>z:print('B')
else:print('TIE')
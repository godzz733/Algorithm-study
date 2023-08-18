n = int(input())
a = []
b = []
for i in range(n):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)
if n == 1: print(0)
else:
    a.sort()
    b.sort()
    print((a[-1]-a[0])*(b[-1]-b[0]))
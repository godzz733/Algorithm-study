import sys;input = sys.stdin.readline
a,b,c = map(int,input().split())
tem = b//10
if tem in [2,4,5,6,8]:
    print(-1)
    exit()
if a%10 == 9:
    print(str(a) + '7' + '1' * (c-5) + str(b))
else:
    print(str(a) + '1' * (c-4) + str(b))
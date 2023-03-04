n,m = map(int, input().split())
x,y = map(int, input().split())
t = int(input())
_x, _y = 0,0
if ((t-(n-x)) // n)%2 == 1:
    _x = (t-(n-x))%n
else:
    _x = n - (t-(n-x))%n
if ((t-(m-y)) // m)%2:
    _y = (t-(m-y))%m
else:
    _y = m - (t-(m-y))%m
print(_x,_y)
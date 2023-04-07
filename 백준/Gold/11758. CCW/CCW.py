x1, y1 = map(int,input().split())
x2, y2 = map(int,input().split())
x3, y3 = map(int,input().split())
def ccw():
    result = (x2-x1)*(y3-y2) - (x3-x2)*(y2-y1)
    if result>0:
        print(1)
        return
    elif result<0:
        print(-1)
        return
    else:
        return print(0)
ccw()
for _ in range(4):
    a,b,c,d,x,y,z,w = map(int,input().split())
    result = 'a'
    if y>d or b>w or z<a or c<x:
        result = 'd'
    elif c==x:
        if d==y or b==w: result = 'c'
        else: result = 'b'
    elif z==a:
        if y==d or b==w: result = 'c'
        else:
            result = 'b'
    elif d==y:
        if c==x or a==z: result = 'c'
        else: result = 'b'
    elif b==w:
        if c==x or a==z: result = 'c'
        else: result = 'b'
    print(result)
a,b,c = map(int, input().split())
x,y,z = 1,1,1
idx = 1
if a == 1 and b == 1 and c == 1:
    print(1)
    exit()
while True:
    idx += 1
    x += 1
    y += 1
    z += 1
    if z == 20: 
        z = 1
    if y == 29:
        y = 1
    if x == 16:
        x = 1
    if x == a and y == b and z == c:
        print(idx)
        break
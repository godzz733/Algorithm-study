import sys
arr = []
draw = 0
for _ in range(19):
    li = [*map(int,input().rstrip().split())]
    arr.append(li)
#가로
def length(x,y,color):
    cnt = 0
    global draw
    try:
        for i in range(5):
            if arr[x][y+i] == color:
                cnt += 1
            if cnt != i+1:
                return
        if 1<=y<=13:
            if arr[x][y+5] == color or arr[x][y-1]==color:
                return
        elif y<=13:
            if arr[x][y+5] == color:
                return
        elif y>=1:
            if arr[x][y-1] == color:
                return
            
        if cnt == 5:
            print(color)
            print(x+1,y+1)
            draw += 1
            return
    except:
        return
#세로
def depth(x,y,color):
    cnt = 0
    global draw
    try:
        for i in range(5):
            if arr[x+i][y] == color:
                cnt += 1
            if cnt != i+1:
                return
        if 1<=x<=13:
            if arr[x+5][y] == color or arr[x-1][y]==color:
                return
        elif x<=13:
            if arr[x+5][y] == color:
                return
        elif 1<=x:
            if arr[x-1][y] == color:
                return
        if cnt == 5:
            print(color)
            print(x+1,y+1)
            draw += 1
            return
    except:
        return
#대각 1
def cross1(x,y,color):
    cnt = 0
    global draw
    try:
        for i in range(5):
            if arr[x+i][y+i] == color:
                cnt += 1
            if cnt != i+1:
                return
        if 1<=x<=13 and 1<=y<=13:
            if arr[x+5][y+5] == color or arr[x-1][y-1] == color:
                return
        elif x<=13 and y<=13:
            if arr[x+5][y+5] == color:
                return
        elif 1<=x and 1<=y:
            if arr[x-1][y-1] == color:
                return
        
        if cnt == 5:
            print(color)
            print(x+1,y+1)
            draw += 1
            return
    except:
        return
#대각 2
def cross2(x,y,color):
    cnt = 0
    global draw
    try:
        for i in range(5):
            if arr[x+i][y-i] == color:
                cnt += 1
            if cnt != i+1:
                return
        if 1<=x<=13 and 5<=y<=17:
            if arr[x+5][y-5] == color or arr[x-1][y+1] == color:
                return
        elif x<=13 and 5<=y:
            if arr[x+5][y-5] == color:
                return
        elif 1<=x and 17>=y:
            if arr[x-1][y+1] == color:
                return
        if cnt == 5:
            print(color)
            print(x+5,y-3)
            draw += 1
            return
    except:
        return
for color in range(1,3):
    for i in range(19):
        for k in range(19):
            length(i,k,color)
            depth(i,k,color)
            cross1(i,k,color)
            cross2(i,k,color)
if draw==0:
    print(0)
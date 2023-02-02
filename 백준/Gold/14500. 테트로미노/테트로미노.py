import sys
input = sys.stdin.readline
n,m = map(int,input().rstrip().split())
arr = []
for i in range(n):
    li = [*map(int,input().rstrip().split())]
    arr.append(li)
result = []
def 직선1(x,y):
    num = 0
    try:
        for i in range(4): #가로
            num += arr[x][y+i]
            if x<0 or y<0:
                return
        result.append(num)
    except:
        return
def 직선2(x,y):
    num = 0
    try:
        for i in range(4): #가로
            num += arr[x+i][y]
            if x<0 or y<0:
                return
        result.append(num)
    except:
        return
def 사각(x,y):
    num = 0
    try:
        for i in range(2): #가로
            num += arr[x][y+i]
            if x<0 or y<0:
                return
        for i in range(2):
            num += arr[x+1][y+i]
        result.append(num)
    except:
        return
def 니은1(x,y):
    num = 0
    try:
        for i in range(3): #가로
            num += arr[x+i][y]
            if x<0 or y<0:
                return
        num += arr[x+2][y+1]
        result.append(num)
    except:
        return
def 니은2(x,y):
    num = 0
    try:
        for i in range(3): #가로
            num += arr[x][y+i]
            if x<0 or y<0:
                return
        num+= arr[x-1][y+2]
        if x-1<0 or y<0:
            return
        result.append(num)
    except:
        return
def 니은3(x,y):
    num = 0
    try:
        for i in range(3): #가로
            num += arr[x-i][y]
            if x-i<0 or y<0:
                return
        num+= arr[x-2][y-1]
        if x-2<0 or y-1<0:
            return
        result.append(num)
    except:
        return
def 니은4(x,y):
    num = 0
    try:
        for i in range(3): #가로
            num += arr[x][y-i]
            if x<0 or y-i<0:
                return
        num+= arr[x+1][y-2]
        if x<0 or y-2<0:
            return
        result.append(num)
    except:
        return
def 니은5(x,y):
    num = 0
    try:
        for i in range(3): #가로
            num += arr[x+i][y]
            if x<0 or y<0:
                return
        num += arr[x+2][y-1]
        if x<0 or y-1<0:
            return
        result.append(num)
    except:
        return
def 니은6(x,y):
    num = 0
    try:
        for i in range(3): #가로
            num += arr[x][y+i]
            if x<0 or y<0:
                return
        num+= arr[x+1][y+2]
        result.append(num)
    except:
        return
def 니은7(x,y):
    num = 0
    try:
        for i in range(3): #가로
            num += arr[x-i][y]
            if x-i<0 or y<0:
                return
        num+= arr[x-2][y+1]
        if x-2<0 or y<0:
            return
        result.append(num)
    except:
        return
def 니은8(x,y):
    num = 0
    try:
        for i in range(3): #가로
            num += arr[x][y-i]
            if x<0 or y-i<0:
                return
        num+= arr[x-1][y-2]
        if x-1<0 or y-2<0:
            return
        result.append(num)
    except:
        return

def 지렁이1(x,y):
    num = 0
    try:
        for i in range(2): #가로
            num += arr[x+i][y]
            if x<0 or y<0:
                return
        num += arr[x+1][y+1]
        num += arr[x+2][y+1]
        result.append(num)
    except:
        return
def 지렁이2(x,y):
    num = 0
    try:
        for i in range(2): #가로
            num += arr[x][y+i]
            if x<0 or y<0:
                return
        num += arr[x-1][y+1]
        num += arr[x-1][y+2]
        if x-1<0 or y<0:
            return
        result.append(num)
    except:
        return
def 지렁이3(x,y):
    num = 0
    try:
        for i in range(2): #가로
            num += arr[x+i][y]
            if x<0 or y<0:
                return
        num += arr[x+1][y-1]
        num += arr[x+2][y-1]
        if x<0 or y-1<0:
            return       
        result.append(num)
    except:
        return
def 지렁이4(x,y):
    num = 0
    try:
        for i in range(2): #가로
            num += arr[x][y+i]
            if x<0 or y<0:
                return
        num += arr[x+1][y+1]
        num += arr[x+1][y+2]
        result.append(num)
    except:
        return
def 손가락1(x,y):
    num = 0
    try:
        for i in range(3): #가로
            num += arr[x][y+i]
            if x<0 or y<0:
                return
        num += arr[x+1][y+1]
        result.append(num)
    except:
        return
def 손가락2(x,y):
    num = 0
    try:
        for i in range(3): #가로
            num += arr[x+i][y]
            if x<0 or y<0:
                return
        num += arr[x+1][y+1]
        result.append(num)
    except:
        return
def 손가락3(x,y):
    num = 0
    try:
        for i in range(3): #가로
            num += arr[x][y+i]
            if x<0 or y+i<0:
                return
        num += arr[x-1][y+1]
        if x-1<0 or y<0:
            return
        result.append(num)
    except:
        return
def 손가락4(x,y):
    num = 0
    try:
        for i in range(3): #가로
            num += arr[x+i][y]
            if x+i<0 or y<0:
                return
        num += arr[x+1][y-1]
        if x<0 or y-1<0:
            return
        result.append(num)
    except:
        return
for x in range(n):
    for y in range(m):
        직선1(x,y)
        직선2(x,y)
        사각(x,y)
        니은1(x,y)
        니은2(x,y)
        니은3(x,y)
        니은4(x,y)
        니은5(x,y)
        니은6(x,y)
        니은7(x,y)
        니은8(x,y)
        지렁이1(x,y)
        지렁이2(x,y)
        지렁이3(x,y)
        지렁이4(x,y)
        손가락1(x,y)
        손가락2(x,y)
        손가락3(x,y)
        손가락4(x,y)
print(max(result))
import sys
input = sys.stdin.readline
arr = []
bingo = []
for _ in range(5):
    li = [*map(int,input().rstrip().split())]
    arr.append(li)
for _ in range(5):
    li = [*map(int,input().rstrip().split())]
    for i in li:
        bingo.append(i)

def bing():
    cnt = 0
    num = 0
    for i in bingo:
        result = 0
        cnt += 1
        for k in range(5):
            for j in range(5):
                if arr[k][j] == i:
                    arr[k][j] = 0
        for q in arr:
            if q.count(0)==5:
                result += 1
        for w in range(5):
            num = 0
            for z in range(5):
                if arr[z][w] == 0:
                    num +=1
            if num == 5:
                result += 1
        num = 0
        for j in range(5):
            if arr[j][j] == 0:
                num +=1
        if num==5:
            result += 1
        num = 0
        for j in range(5):
            if arr[j][4-j] == 0:
                num+=1
        if num==5:
            result += 1
        num = 0
        if result>=3:
            return cnt
print(bing())
            
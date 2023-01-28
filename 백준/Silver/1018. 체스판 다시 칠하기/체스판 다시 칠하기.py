import sys
input = sys.stdin.readline
n,m = map(int,input().split())
w = ['W','B','W','B','W','B','W','B']
b = ['B','W','B','W','B','W','B','W']
arr = []
result = []
for _ in range(n):
    li = str(input())
    arr.append(list(li))
def sq(x,y):
    global result
    count = 0
    count1 = 0
    for i in range(8):
        for k in range(8):
            if i%2==0:
                if arr[x+i][y+k] != w[k]:
                    count +=1
            else:
                if arr[x+i][y+k] != b[k]:
                    count1 +=1
    result.append(count+count1)
    
    return 1
def sp(x,y):
    global result
    count = 0
    count1 = 0
    for i in range(8):
        for k in range(8):
            if i%2==0:
                if arr[x+i][y+k] != b[k]:
                    count +=1
            else:
                if arr[x+i][y+k] != w[k]:
                    count1 +=1
    result.append(count+count1)
    return 1
for i in range(n-7):
    for j in range(m-7):
        sq(i,j)
        sp(i,j)
print(min(result))
    
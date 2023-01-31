import sys
sys.setrecursionlimit(10000)
n,m= map(int,input().rstrip().split())
arr = [*map(int,input().rstrip().split())]
arr.sort()
stack = []
li = []
def back():
    if len(li)==m:
        print(*li)
        return

    for i in range(n):
        if arr[i] not in li:
            li.append(arr[i])
            back()
            li.pop()
if m==1:
    for i in arr:
        print(i)
else:
    back()

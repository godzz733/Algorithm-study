import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    dic = {}
    a = int(input())
    arr = [*map(int,input().split())]
    for i in arr:
        dic[i] = 1
    b = int(input())
    arr1 = [*map(int,input().split())]
    for i in arr1:
        if i in dic:
            print(1)
        else:
            print(0)
    
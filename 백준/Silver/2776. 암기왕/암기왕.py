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
            sys.stdout.write(str(1) + "\n")
        else:
            sys.stdout.write(str(0) + "\n")
    
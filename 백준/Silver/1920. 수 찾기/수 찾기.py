import sys
a=1
t1 = int(input())
arr1 = list(set([*map(int,sys.stdin.readline().split())]))
arr1.sort()
t2 = int(input())
arr2 = [*map(int,sys.stdin.readline().split())]

for i in arr2:
    if i in arr1:
        print(1)
        continue
    else:
        print(0)

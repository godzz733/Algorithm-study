import sys
a = int(input())
arr = [*map(int, sys.stdin.readline().split())]
b = int(input())
arr1 = [*map(int, sys.stdin.readline().split())]
dic = {}
for i in arr:
    dic[i] = 0

for i in range(b):
    if arr1[i] in dic:
        arr1[i] = 1
    else:
        arr1[i] = 0
print(*arr1) 

import sys;input = sys.stdin.readline
import math
arr = [['  *  ', ' * * ', '*****'],[],[],[],[],[],[],[],[],[],[],[],[],[]]
n = int(input())
tem = int(math.log2((n//3)))
for k in range(1,tem+1):
    num = 3 * (2 ** (k-1))
    for i in range(num):
        arr[k].append(' ' * num + arr[k-1][i] + ' ' * num)
    for i in range(num):
        arr[k].append(arr[k-1][i] + ' ' + arr[k-1][i])
for i in range(n):
    print(arr[tem][i])

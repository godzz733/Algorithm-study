import sys
a = int(input())
arr = []
for i in range(a):
    n, k = map(int, sys.stdin.readline().split())
    arr.append([n,k])

arr.sort(key=lambda x:(x[1],x[0]))
[print(' '.join(list(map(str,i)))) for i in arr]

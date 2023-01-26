import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = [*map(int,input().split())]
for i in range(1,n):
    arr[i] = arr[i-1] + arr[i]
for i in range(m):
    a,b = map(int,input().split())
    if a==1:
        print(arr[b-1])
    else:
        print(arr[b-1]-arr[a-2])
        
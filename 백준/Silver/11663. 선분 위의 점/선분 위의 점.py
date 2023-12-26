import sys;input = sys.stdin.readline
from bisect import bisect_left, bisect_right
n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
line = [tuple(map(int,input().split())) for _ in range(m)]
for x,y in line:
    print(bisect_right(arr,y)-bisect_left(arr,x))
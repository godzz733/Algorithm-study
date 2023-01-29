import sys
import heapq as hep
input = sys.stdin.readline
n = int(input())
arr = []

for _ in range(n):
    a = int(input())
    if a!=0:
        hep.heappush(arr,a)
    else:
        if arr==[]:
            print(0)
        else:
            print(hep.heappop(arr))


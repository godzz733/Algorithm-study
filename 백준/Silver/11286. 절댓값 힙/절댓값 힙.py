import heapq as heq
import sys
input = sys.stdin.readline
print = sys.stdout.write
arr = []
for _ in range(int(input())):
    x = int(input())
    if not x: print(str(heq.heappop(arr)[1]) + "\n") if arr else print('0\n')
    else: heq.heappush(arr, (abs(x), x))
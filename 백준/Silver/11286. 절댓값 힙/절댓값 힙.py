import heapq as heq
import sys
input = sys.stdin.buffer
print = sys.stdout.write
input.readline()
inp = list(map(int, input.read().splitlines()))
arr = []
input.readline()
for x in inp:
    if not x: print(str(heq.heappop(arr)[1]) + "\n") if arr else print('0\n')
    else: heq.heappush(arr, (abs(x), x))
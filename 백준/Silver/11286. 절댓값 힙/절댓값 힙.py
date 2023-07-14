import heapq as heq, sys
arr = []
for _ in range(int(input())):
    x = int(sys.stdin.readline())
    if not x: print(heq.heappop(arr)[1]) if arr else print(0)
    else: heq.heappush(arr, (abs(x), x))
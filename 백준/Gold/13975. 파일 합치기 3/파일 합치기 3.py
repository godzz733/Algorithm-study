import sys; input = sys.stdin.readline
import heapq as h

for _ in range(int(input())):
    n = int(input())
    q = []
    ans = 0
    for i in map(int,input().split()):
        h.heappush(q,i)
    for _ in range(n-1):
        t = h.heappop(q) + h.heappop(q)
        ans += t
        h.heappush(q,t)
    print(ans)
import sys;input = sys.stdin.readline
import heapq as h
n = int(input())
q = []
tem = 0
for i in range(n):
    a = int(input())
    if not i:
        tem = a
        continue
    h.heappush(q, (-a,i))

ans = 0
while q:
    a, i = h.heappop(q)
    if -a < tem:break
    ans += 1
    tem += 1
    h.heappush(q, (a+1,i))
print(ans)
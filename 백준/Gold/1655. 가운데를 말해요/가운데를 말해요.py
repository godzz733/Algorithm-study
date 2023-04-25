import heapq, sys
input = sys.stdin.readline
n = int(input())
q1,q2 = [], []
for _ in range(n):
    if len(q1) == len(q2):
        heapq.heappush(q1,-int(input()))
    else:
        heapq.heappush(q2,int(input()))
    if q2 and q2[0] < -q1[0]:
        a = heapq.heappop(q1)
        b = heapq.heappop(q2)
        heapq.heappush(q1,-b)
        heapq.heappush(q2,-a)
    print(-q1[0])
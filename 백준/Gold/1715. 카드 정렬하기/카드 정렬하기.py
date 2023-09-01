import sys,heapq
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
heapq.heapify(arr)
ans = 0
for i in range(n-1):
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    ans += a+b
    heapq.heappush(arr,a+b)
print(ans)
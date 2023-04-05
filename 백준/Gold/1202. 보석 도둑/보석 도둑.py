import heapq
n, m = map(int,input().split())
q = [] # 우선순위 큐
jew = []
bag = []
for _ in range(n):
    a, b = map(int,input().split()) # 무게, 가격
    jew.append((a,b))
jew.sort()
for _ in range(m):
    bag.append(int(input()))
bag.sort()
idx = 0
result = 0
for i in bag:
    while idx<n and jew[idx][0] <= i:
        heapq.heappush(q,(-jew[idx][1]))
        idx += 1
    if q:
        result += -heapq.heappop(q)
print(result)
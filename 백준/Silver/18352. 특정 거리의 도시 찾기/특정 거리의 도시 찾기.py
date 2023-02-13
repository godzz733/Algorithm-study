import heapq

n, m, k, start = map(int, input().split())
INF = int(1e9)
distance = [INF] * (n+1)
graph =  [[] for _ in range(n+1)]
result = []
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1))

def dik(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dik(start)

for i in range(1,n+1):
    if distance[i] == k:
        result.append(i)

if not result:
    print(-1)
else:
    for i in result:
        print(i)

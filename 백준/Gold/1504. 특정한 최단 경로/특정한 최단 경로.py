import heapq

n, m = map(int, input().split())
INF = int(1e9)
distance1 = [INF] * (n+1) # start = 1
distance2 = [INF] * (n+1) # start = v1
distance3 = [INF] * (n+1) # start = v2

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1, v2 = map(int, input().split())
def dik(distance, start):
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

dik(distance1, 1)
dik(distance2, v1)
dik(distance3, v2)
if distance1[v1] + distance2[v2] + distance3[n] >= INF and distance1[v2] + distance3[v1] + distance2[n] >= INF:
    print(-1)
else:
    if distance1[v1] + distance2[v2] + distance3[n] < distance1[v2] + distance3[v1] + distance2[n]:
        print(distance1[v1] + distance2[v2] + distance3[n])
    elif distance1[v1] + distance2[v2] + distance3[n] > distance1[v2] + distance3[v1] + distance2[n]:
        print(distance1[v2] + distance3[v1] + distance2[n])
    else:
        print(distance1[v1] + distance2[v2] + distance3[n])
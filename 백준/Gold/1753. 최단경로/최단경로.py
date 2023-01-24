import sys
INF = int(1e9)
v,e = map(int ,input().split())
start = int(input())
visted = [False] * (v+1)
distance = [INF] * (v+1)
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

def get_lowest_idx():
    index = 0
    min_distance = INF
    for i in range(1,v+1):
        if distance[i] < min_distance and not visted[i]:
            min_distance = distance[i]
            index = i
    return index

def dik(start):
    distance[start] = 0
    visted[start] = True
    
    for i in graph[start]: #  방문처리
        if distance[i[0]] > i[1]:
            distance[i[0]] = i[1]
    
    for k in range(v-1): 
        now = get_lowest_idx()
        visted[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
dik(start)
for i in range(1,v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
import sys
INF = int(1e9)
v,e = map(int ,input().split()) # 노드 개수와 간선 개수를 받음
start = int(input()) # 어디서 시작할건지 체크
visted = [False] * (v+1) #방문체크 0번쨰는 신경안쓰고 v+1 까지 기록남김 (인덱스를 1부터 하려고)
distance = [INF] * (v+1) #마찬가지로 0번쨰는 신경 안쓰려고 v+1까지 (인덱스를 1부터 하려고))
graph = [[] for _ in range(v+1)] #간선 저장할 데이터 선언
for _ in range(e):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c)) #a 번 노드에서 b번 노드로 가는 거리 c를 저장

def get_lowest_idx(): #지금 상황에서 방문한적 없고 나와 가장 가까운 노드를 찾을거임
    index = 0
    min_distance = INF
    for i in range(1,v+1):
        if distance[i] < min_distance and not visted[i]: #방문을 안햇고 나와의 거리가 가장 짧다면
            min_distance = distance[i]
            index = i
    return index #나와 가장 거리가 가까운 index를 반환함

def dik(start):
    distance[start] = 0 #시작지점 거리를 0으로 설정하고 방문처리
    visted[start] = True
    
    for i in graph[start]: #  나와 연결된 노드들의 거리를 저장
        if distance[i[0]] > i[1]: #이문제에서는 두 노드사이의 간선이 여러개일 수도 있어서 처리해줌
            distance[i[0]] = i[1]
    
    for k in range(v-1): #시작점 빼고, 0 빼서 v+1 에서 v -1이 됨
        now = get_lowest_idx() #나와 가장 가까운 거리의 노드의 인덱스
        visted[now] = True #방문처리
        for j in graph[now]: #지금 노드에 저장된 간선을 다 검사
            cost = distance[now] + j[1] #지금나까지 올떄까지의 거리와 다른 노드와의 거리를 더함
            if cost < distance[j[0]]: #이때 그 다른 노드의 거리가 지금 거리보다 크다면 지금거리를 저장
                distance[j[0]] = cost
dik(start)
for i in range(1,v+1): #시작점부터 돌면서 각 노드들의 최소값을 출력
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])

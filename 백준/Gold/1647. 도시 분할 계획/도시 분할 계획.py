def find_parent(parent, x):
    if parent[x] != x: #만약 지금 노드의 부모 노드가 나 자신이 아니라면
        parent[x] = find_parent(parent, parent[x]) #부모 노드를 검색함
    return parent[x]

def union_parent(parent, a, b): #a, b가 연결 되어있다는 정보를 입력 받은 후 둘을 합칠거임
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: #일반적으로 더 작은 노드를 부모 노드로 잡으므로 a<b일때는 a를 부모 노드로 잡음
        parent[b] = a
    else:
        parent[a] = b
n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(0, n+1): #각 노드를 일단 자기 자신으로 초기화
    parent[i] = i
edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) #간선의 비용으로 정렬할거기 때문에 cost를 맨 앞에 배치
result = 0
edges.sort() #최소 비용을 구하기 위해 정렬
last = 0 #이후 두개의 마을로 쪼갤 때 사용

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b): # 만약 두 노드의 부모 노드가 다르다면
        union_parent(parent, a, b) #한개의 부모노드로 연결
        result += cost #결과값에 거리 비용을 추가
        last = cost #문제가 두 마을로 쪼갤 때이므로 가장 큰 간선비용을 가진걸 미리 구해놈
print(result - last) #이때 쪼갤 때 가장 비용이 비싼 간선을 끊으면 두 마을로 쪼개지고 이때 최소 마을 유지비용은 전체에서 이것을 뺀것임

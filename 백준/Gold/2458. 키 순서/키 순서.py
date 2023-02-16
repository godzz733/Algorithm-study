n, m = map(int,input().split())
distance = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    distance[a][b] = 1 # 자기보다 큰 번호 까지 거리가 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j: # 자기 자신은 0으로 초기화
                distance[i][j] = 0
                continue
            if distance[i][k] == 1 and distance[k][j] == 1: #만약 어떤 경로를 거쳐 자기로 왓다면, 단 두 경로가 모두 연결되어 있어야함
                distance[i][j] = 1 # 이 뜻은 어떤 경로를 거쳐서 자기보다 큰 경로를 찾은거임

cnt = 0
for i in range(1,n+1):
    num = 0
    for j in range(1,n+1):
        num += distance[i][j] + distance[j][i] # 만약 자기보다 큰 노드가 있거나, 작은 노드가 있으면 +1
    if num == n-1: # 자기보다 크거나 작은 노드가 자기 자신을 제외한 노드의 갯수 n-1 만큼 있다면 키 순서를 알 수 있음
        cnt += 1 # 결과에 1 추가
print(cnt)
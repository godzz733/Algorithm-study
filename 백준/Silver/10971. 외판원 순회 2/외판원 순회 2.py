n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[None] * (1<<n) for _ in range(n)] # 비트로 n개의 도시의 방문 여부를 표시
arrive = (1<<n) -1 # 만약 다 돌앗다면 == 비트가 다 1로 채워져 있다면 종료
INF = float('inf')

def find_path(last,visit):
    if visit == arrive: # 모든 도시를 다 돌았다면 출발지로 돌아가고 마무리
        return arr[last][0] or INF # 만약 도착지로 돌아갈 수 없다면 불가능
    
    if visited[last][visit] is not None: # 만약 이미 이 경로를 돌았다면 dp로 빠르게 처리
        return visited[last][visit]
     
    temp = INF
    for city in range(n): # 각 도시를 돌건데
        if visit & (1<<city) == 0 and arr[last][city]: # 만약 아직 돌지 않았고, 그 도시를 갈 수 있다면
            temp = min(temp, find_path(city, visit | (1<<city)) + arr[last][city]) # 재귀적으로 방문하는데 이때 도시와의 거리를 더해서 표시
    visited[last][visit] = temp # 전부 해보면 최소값을 알 수 있으므로 dp 테이블에 저장
    return temp # 그 값을 리턴

print(find_path(0,1<<0)) # 0부터 시작할거고 0을 돌고 시작하기 떄문에 0001(0은 n-1 개있는거임)로 표시
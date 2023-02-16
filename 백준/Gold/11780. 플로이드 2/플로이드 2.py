n = int(input())
m = int(input())
INF = int(1e9)
arr = [[INF] * (n+1) for _ in range(n+1)]
visited = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a][b] = min(arr[a][b],c)

for i in range(1,n+1):
    arr[i][i] = 0
def find_path(i,j):
    if visited[i][j] == 0: # 만약 i->j가 k를 거쳐가지 않았다면 그냥 빈 리스트를 리턴
        return []
    k = visited[i][j] # 거쳐간 k를 불러옴
    return find_path(i,k) + [k] + find_path(k,j) #현재 k를 중앙에 저장하고 다시 i->k 까지 거쳐온 경로, k->j 까지 거쳐온 경로를 양 옆에 붙여줌, 만약 i==k 또는 k==j라면 0이니까 빈리스트를 리털할거임

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i][j] > arr[i][k] + arr[k][j]:
                arr[i][j] = arr[i][k] + arr[k][j]
                visited[i][j] = k # 만약 i,j가 k를 거쳐 갓다면 저장

for i in range(1,n+1): # 그냥 문제의 출력형식
    for j in range(1,n+1):
        print(arr[i][j] if arr[i][j] != INF else 0, end=' ')
    print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if arr[i][j] in [0,INF]:
            print(0)
            continue
        path = [i] + find_path(i,j) + [j] #find_path함수에서는 i와 j가 아니라 그 사이 거쳐운 경로만 리턴하므로 양옆에 [i] 와 [j]를 붙여주고 find_path를 함
        print(len(path), end=' ')
        print(*path)

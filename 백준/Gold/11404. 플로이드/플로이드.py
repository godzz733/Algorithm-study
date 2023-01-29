import sys
input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())
INF = int(1e9)
arr = [[INF] * (n+1) for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int, input().rstrip().split())
    if arr[a][b] > c: #버스가 여러개 있을 수 있으니 작은거만 적용
        arr[a][b] = c
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):            
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b]) 
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b or arr[a][b]==int(1e9): # 자기 자신으로 가는경우, 갈 수있는 길이 없어 INF인 경우
            arr[a][b] = 0              
for i in range(1,n+1):
        print(' '.join(map(str , arr[i][1:n+1])))

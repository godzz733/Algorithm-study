n = int(input())
m = int(input())
arr = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i][k] == 1 and arr[k][j] == 1: # 자기보다 크거나 작은게 있다면
                arr[i][j] = 1 # 1을 더함
for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        if arr[i][j] + arr[j][i] == 0: # 어떤 방향으로든 가르키는게 없다면
            cnt += 1 # 나와의 상하 관계를 모르니까 비교 결과를 알 수 없음
    print(cnt-1) # 자기 자신 (i==j)은 0이니까 하나 제외
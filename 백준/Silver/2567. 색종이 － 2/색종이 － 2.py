n = int(input())
arr = [[0] * 102 for _ in range(102)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
result = 0
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            arr[i][j] = 1
for i in range(1,101):
    for j in range(1,101):
        if arr[i][j] == 1: # 둘레에 있을 때만, 사각형 내부면 무조건 cnt = 4니까
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                cnt += arr[nx][ny]
            if cnt == 3: # 둘레면 삼면이 1임
                result += 1
            elif cnt == 2: # 모서리면 두면이 1임
                result += 2


print(result)

dx = [1,0,-1,0]
dy = [0,1,0,-1]
def check(x,y): # 갈수 있는 곳과 거리 측정
    direction = [0,0,0,0] # 어떤 방향으로 갈 수 있고 그 방향까지의 길이는 몇인지 체크
    for d in range(4):
        now_x, now_y = x, y
        length = 0
        while 0<now_x<n-1 and 0<now_y<n-1:
            now_x += dx[d]
            now_y += dy[d]
            length += 1
            if arr[now_x][now_y]: # 그 방향에 다른 프로세서가 잇거나 전선이 있으면 넘어감
                break
        else:
            direction[d] = length # 갈 수 있는 방향으로 가는 길이
    return direction

def connect(x,y,d): # 선 연결, 해제 하는 함수
    now_x, now_y = x, y
    while 0 < now_x < n - 1 and 0 < now_y < n - 1:
        now_x += dx[d]
        now_y += dy[d]
        arr[now_x][now_y] ^= 1 # 비트연산자로 0과 1을 바꿔줌, 즉 연결 또는 해제

def recur(cur, min_sum, result_cnt): # cur은 연결 시킬 코어 총 갯수, min_sum은 최소 전선 길이, result_cnt는 최대 연결 코어 수
    global result
    if result[0] < result_cnt: # 연결할 수 있는 코어가 많다면
        result[0] = result_cnt # 값 재설정
        result[1] = min_sum
    elif result[0] == result_cnt: # 코어는 같은데 길이가 더 짧을 때
        if result[1] > min_sum:
            result[1] = min_sum
    if cur == cnt: # 전부 연결 햇으면 return
        return
    x, y = core[cur][0], core[cur][1] # 현재 코어의 x,y 좌표를 받아옴
    direction = check(x,y) # 갈 수 있는 방향 체크
    for d in range(4):
        if not direction[d]: # 갈 수 없으면 그냥 안감
            continue
        connect(x,y,d) # 갈 수 있으면 연결 해봄
        recur(cur+1,min_sum+direction[d],result_cnt+1) # 연결 해본 뒤 다음 코어 실행
        connect(x,y,d) # 연결 해제
    recur(cur+1,min_sum,result_cnt) # 연결 안하고 그냥 가보기
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = [0,0] # 최대 연결 수, 최소 전선 길이
    core = []
    cnt = 0 
    for i in range(1,n-1): # 어처피 최소 길이를 찾은거라서 가장자리는 아예 안가도 됨
        for j in range(1,n-1):
            if arr[i][j]:
                core.append((i,j))
                cnt += 1
    recur(0,0,0) # 처음 코어부터 다 돌아봄
    print(f'#{tc} {result[1]}')

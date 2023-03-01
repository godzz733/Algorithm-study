from collections import deque
def mag(n,m):
    회전 = [(n,m)] # 회전 시킬거임 회전 자석번호와 회전 방향 
    ori,ro,i = n,m,n-1 # 기준 자석과 그 방향, 그리고 기준으로부터 왼쪽꺼 부터 확인할거임
    while 0<=i:
        if arr[ori][6] != arr[i][2]: # 맞닿아 있는 극이 서로 다르다면 
            회전.append((i,-ro)) # 회전할 자석에 추가와 기준의 반대 방향으로 방향 설정
            ori,ro = i,-ro # 그 다음 자석을 기준으로 바꾸고 방향도 반대로 바꿈
            i -= 1 # 그 왼쪽을 탐색
        else:
            break
    ori,ro,i = n,m,n+1 # 위와 다르게 오른쪽을 탐색
    while i<4:
        if arr[ori][2] != arr[i][6]:
            회전.append((i,-ro))
            ori,ro = i, -ro
            i += 1
        else:
            break
    for i,ro in 회전: # 회전 시킴
        q = deque(arr[i])
        q.rotate(ro)
        arr[i] = list(q)
t = int(input())
for tc in range(1,t+1):
    k = int(input())
    arr = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(k):
        n, m = map(int,input().split())
        mag(n-1,m)
    result = 0
    for i in range(4): # 맨 위가 s극이면 2의 i승만큼 점수 추가 
        if arr[i][0]:
            result += 2**i
    print(f'#{tc} {result}')
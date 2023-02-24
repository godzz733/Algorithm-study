from collections import deque
result = [0] * (100001) # 이동 횟수의 최솟값을 저장할 딕셔너리

n, m = map(int, input().split())
key = cnt = 0 # key는 반복문을 멈추기 위함
q = deque()
visited = set() # 방문
lst = set() # 방문처리, q에 넣는거 처리한 리스트
result[n] = [n]
lst.add(n)
visited.add(n)
while lst:
    q.extend(lst) # 횟수 한번당 갈 수 있는 전체를 도달하고 방문처리도 한번에 하기 위함
    for i in lst:
        visited.add(i)
    lst.clear()
    cnt += 1
    while q:
        x = q.popleft()
        if x == m: # 도착햇으면 그 횟수까지만 하고 종료
            key += 1
            continue
        else:
            if 0<=x<100001:
                if x-1 not in visited and x-1>=0:
                    lst.add(x-1)
                    if not result[x-1]:
                        result[x-1] = x # 만약 여기를 처음 도착하면 어디서 부터 왓는지 기록함
                if x+1 not in visited and x+1 <= 100000:
                    lst.add(x+1)
                    if not result[x+1]:
                        result[x+1] = x

                if x*2 not in visited and x*2<100001:
                    lst.add(x*2)
                    if not result[x*2]:
                        result[x*2] = x
    if key:
        break
print(cnt-1)
if n==m: # 출발, 도착이 같으면 도착지만 출력
    print(n)
else:
    a = -1
    ans = []
    ans.append(m)
    while a != n:
        a = result[m] # 재귀적으로 도착지가 어디서 왓는지를 역추적해서 출발지에 도달할때까지 함
        m = a
        ans.append(a)
    print(*ans[::-1])


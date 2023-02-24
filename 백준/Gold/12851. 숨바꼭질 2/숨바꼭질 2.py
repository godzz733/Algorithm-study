from collections import deque
result = [0] * (200001) # 그 위치에 몇번 도착 햇는지
n, m = map(int, input().split())
result[n] = 1
key = cnt = 0 # key는 반복문을 멈추기 위함, cnt는 점프 횟수
q = deque()
visited = set() # 방문
lst = set() # 방문처리, q에 넣는거 처리한 리스트
lst.add(n)
visited.add(n)
while lst:
    q.extend(lst) # 횟수 한번당 갈 수 있는 전체를 도달하고 방문처리도 한번에 하기 위함
    cnt += 1 # 1회 점프
    for i in lst:
        visited.add(i)
    lst.clear()
    while q:
        x = q.popleft()
        if x == m: # 도착햇으면 그 횟수까지만 하고 종료
            key += 1
            continue
        else:
            if 0<=x<100001:
                if x-1 not in visited:
                    lst.add(x-1)
                    result[x-1] += result[x]
                if x+1 not in visited:
                    lst.add(x+1)
                    result[x+1] += result[x]
                if x*2 not in visited and x*2<100001:
                    lst.add(x*2)
                    result[x*2] += result[x]
    if key:
        break
print(cnt - 1)
print(result[m])

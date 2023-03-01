def honey(x,y): # 가능한 꿀 채취를 다 기록할거임
    honey_sum = 0 # 어떤 한 구간에서 가능한 최대 수확량
    lst = arr[x][y:y+m] # 그 구간
    honey_list = find_honey(lst) # 순열을 통해서 어떤 구간에서 채취 가능한 경우를 다 기록해서 넘겨받음
    for k in honey_list:
        a = 0
        for i in k: # 꿀의 제곱을 저장
            a += i**2
        if a > honey_sum: # 지금까지 가능한 최대보다 크다면 변경
            honey_sum = a
    return [x,y,honey_sum] # 채취한 꿀의 세로, 가로, 채취량을 리턴함
def find_honey(lst): # 어떤 구간에서 채취 가능한 꿀의 경우의 수를 찾아냄 (순열)
    honey_list = []
    for i in range(1<<m): # 비트 오퍼레이터 사용
        li = []
        for j in range(m):
            if i & (1<<j):
                li.append(lst[j])
        if li and sum(li) <= c: # 채취 가능할 때만 넘길거임
            honey_list.append(li)
    return honey_list
t = int(input())
for tc in range(1,t+1):
    result = 0
    result_x = [0,0]
    comb = []
    n, m, c =map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    for i in range(n): # 가능한 모든 경우의 꿀을 다 구함
        for j in range(n-m+1):
            comb.append(honey(i,j))
    for i in range(len(comb)-1):
        for j in range(i+1,len(comb)):
            if comb[i][0] == comb[j][0]: # 만약 세로가 같다면 가능한 가로의 경우의 수를 골라서 비교
                if comb[j][1] - comb[i][1] >= m:
                    if result < comb[i][2] + comb[j][2]:
                        result = comb[i][2] + comb[j][2]
                        result_x = [comb[i],comb[j]]
            elif comb[i][0] != comb[j][0]: # 세로가 다르다면 가로는 상관 없으므로 그냥 비교
                if result < comb[i][2] + comb[j][2]:
                    result = comb[i][2] + comb[j][2]
                    result_x = [comb[i],comb[j]]
    print(f'#{tc} {result}')
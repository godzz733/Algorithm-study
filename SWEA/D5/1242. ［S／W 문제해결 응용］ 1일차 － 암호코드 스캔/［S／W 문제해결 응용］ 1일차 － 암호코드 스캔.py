passw = [['000','11','0','1'],['00','11','00','1'],['00','1','00','11'],['0','1111','0','1'],['0','1','000','11']
         ,['0','11','000','1'],['0','1','0','1111'],['0','111','0','11'],['0','11','0','111'],['000','1','0','11']]
password = {}
for j in range(10): # 모든 조합을 다 만듬 (여기선 100이면 가능한듯)
    for i in range(100):
        word = ''
        for k in range(4):
            word += passw[j][k] * i
        if word:
            password[word] = f'{j}'
t = int(input())
for tc in range(1,t+1):
    n, m = map(int, input().split())
    pre_arr = set()
    arr = set()
    real_password = set()
    real_result = 0

    for _ in range(n): # 16진수 암호 찾기
        lst = ''.join(list(str(input())))
        if format(int(lst,16),'b'):
            a = list('000000000000000000000000' + format(int(lst,16),'b')) # 앞에 0이 몇개일지 몰라서 일단 많이 붙임
            while a:
                if a[-1] == '0': # 암호는 무조건 1로 끝나기 때문에 모든 0을 제거
                    a.pop()
                else:
                    pre_arr.add(''.join(a))
                    break

    for j in pre_arr:
        visited = [] # 방문한 범위는 방문 안할거임
        if not int(j): # 그냥 0만 있으면 안봄
            continue
        for k in range(1,(len(j) // 56)+1): # 최대 암호길이 설정
            i = cnt = 0
            li = []
            pre = 0
            while i < len(j)-k*7: # 암호의 최대 길이만큼 앞 까지만 검색하면 됨
                if j[i] != '0': # 암호는 무조건 0으로 시작하므로 0이 아니면 한칸 뒤로
                    i += 1
                    continue
                elif j[i+k*7-1] == '0': # 암호는 무조건 1로 끝나므로 1이 아니면 한칸 뒤로
                    i += 1
                    continue
                if i in visited: # 방문 햇다면
                    if cnt >= len(visited): # 만약 방문의 마지막이면 그냥 한칸만 뒤로
                        i += 1
                    else:
                        i = visited[cnt]+1 # 방문한 곳이라면 방문한곳 한칸 뒤로 감
                        cnt += 1
                    continue
                pre = i # 어디서 시작햇는지 기록
                if ''.join(j[i:i+7*k]) in password: # 만약 여기부터 암호가 가능하면
                    st = i 
                    for q in range(8): # 암호 8자리를 만들어볼거임
                        try:
                            li.append(password[''.join(j[i:i+7*k])])
                            i += 7*k
                        except: # 만약 암호가 아닌거엿다면 그냥 다 초기화
                            li.clear()
                            i = pre + 1 # 아까 방문 시작한 바로 앞에서 다시 탐색
                            break
                else:
                    i += 1 # 아무것도 아니면 그냥 한칸 뒤로
                if len(li) == 8: # 만약 암호가 완성 됫다면
                    real_password.add(''.join(li))
                    li.clear()
                    fi = i
                    visited.append(st) #방문 맨 앞
                    visited.append(fi) #방문 맨 뒤
                    visited.sort() # 방문 처리한걸 정렬해줘야 쓸 수 잇음
    for i in real_password:
        check = 0
        for j in range(0,7):
            if not j%2: # 홀수면 3배해서 더함
                check += int(i[j]) * 3
            else: # 짝수는 그냥 더함
                check += int(i[j])
        check += int(i[7]) # 홀수지만 검증 코드라 그냥 더함
        if not check%10: # 10의 배수면 결과값에 더함
            real_result += sum(list(map(int,list(i))))

    print(f'#{tc} {real_result}')
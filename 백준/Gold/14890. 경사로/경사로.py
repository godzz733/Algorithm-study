def road(arr):
    cnt = 1
    for i in range(1,n):
        if arr[i] == arr[i-1]: # 이전의 높이와 같다면
            cnt += 1
        elif arr[i] - arr[i-1] == 1 and cnt >= x: # 이전 높이보다 한칸 높고 길이가 x보다 길면
            cnt = 1 # 건설 가능
        elif arr[i-1] - arr[i] == 1 and cnt>= 0: # 이전 높이보다 한칸 낮고 길이가 0보다 크면
            cnt = -x + 1 # 결과값에서 cnt가 0보다 같거나 크면 가능한 걸로 할건데 이때 한칸 낮다는 건 오른쪽에서 왓을 떄 건설이
            # 가능하다는 것이고 이는 cnt가 현재를 포함하여 활주로 길이보다 길어야 하므로 활주로 길이인  -x와 현재 길이인 1을 더해서 cnt가 0보다 같거나 크려면 지금과 같은 거리가 하나 더 있어야 함을 의마함
        else:
            return 0 # 이외의 경우는 다 틀림
    if cnt>= 0: # 만약 문제가 없다면 cnt가 0보다 큼
        return 1
    return 0



n, x = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0
for i in range(n): # 가로 검사
    result += road(arr[i])
for i in range(n): # 세로 검사
    temp = []
    for j in range(n):
        temp.append(arr[j][i])
    result += road(temp)
print(result)
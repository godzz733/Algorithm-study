from collections import deque
def solution(alp, cop, problems):
    a = alp
    b = cop
    arr = []
    needa = 0
    needb = 0
    for i in problems:
        # for j in arr:
        #     if i[2] == j[2] and i[3] == j[3] and i[4] <= j[4]:
        #         arr[j] = i
        #         break
        if i[2] == 0 and i[3] == 0:
            continue
        arr.append(i)
        needa = max(needa, i[0])
        needb = max(needb, i[1])
    visited = [[987654321] * (200) for _ in range(200)]
    answer = 0
    answer = dfs(needa,needb,arr,visited,a,b)
    return answer

def dfs(needa, needb,arr,visited, a, b):
    answer = 987654321
    q = deque()
    q.append((a,b,0)) #alp,cop,cost
    while q:
        alp, cop, cost = q.popleft()
        if alp + 1 < needa and visited[alp+1][cop] > cost+1:
            visited[alp+1][cop] = cost+1
            q.append((alp+1,cop,cost+1))
        if cop + 1 < needb and visited[alp][cop+1] > cost+1:
            visited[alp][cop+1] = cost+1
            q.append((alp,cop+1,cost+1))
        if alp >= needa and cop >= needb:
            answer = min(answer,cost)
        for i in arr:
            if alp < i[0] or cop < i[1]:
                continue
            alp_t = alp + i[2]
            cop_t = cop + i[3]
            if alp_t > needa:
                alp_t = needa
            if cop_t > needb:
                cop_t = needb
            cost_t = cost + i[4]
            if visited[alp_t][cop_t] > cost_t:
                visited[alp_t][cop_t] = cost_t
                q.append((alp_t,cop_t,cost_t))
    return answer
        

            
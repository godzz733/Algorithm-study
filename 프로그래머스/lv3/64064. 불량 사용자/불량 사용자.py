ans_set = set()
def solution(user_id, banned_id):
    arr = [[] for _ in range(len(banned_id))]
    dic = {}
    for i in range(len(user_id)):
        dic[user_id[i]] = str(i)
    for j in range(len(banned_id)):
        for i in user_id:
            key = 1
            if len(i) != len(banned_id[j]):
                continue
            for k in range(len(i)):
                if banned_id[j][k] == "*":
                    continue
                elif i[k] != banned_id[j][k]:
                    key = 0
                    break
            if key == 1:
                arr[j].append(i)
        
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = dic[arr[i][j]]
    dfs(0,arr,len(banned_id),[])
    answer = len(ans_set)
    print(arr)
    print(ans_set)
    return answer
def dfs(cnt,arr,n,ans):
    if cnt == n:
        if len(ans) == n:
            ans_set.add(''.join(sorted(ans)))
            return
    for i in range(len(arr[cnt])):
        if arr[cnt][i] not in ans:
            ans.append(arr[cnt][i])
            dfs(cnt+1,arr,n,ans)
            ans.pop()
    
            
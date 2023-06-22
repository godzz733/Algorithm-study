arr = [0]
set1 = set()
set2 = set()
def solution(cards):
    global arr,set1,set2
    arr += cards
    answer = 0
    for i in range(1,len(cards)+1):
        set1 = set()
        dfs(i)
        for j in range(1,len(cards)+1):
            set2 = set()
            dfs2(j)
            answer = max(answer,len(set1)*len(set2))
    return answer
def dfs(x):
    global set1
    if x in set1:
        return
    set1.add(x)
    dfs(arr[x])
    return
def dfs2(x):
    global set2,set1
    if x in set2 or x in set1:
        return
    set2.add(x)
    dfs2(arr[x])
    return
    

def dfs(x,result):
    global _max
    if x == 11:
        if _max < result:
            _max = result
            return
        return

    for i in range(11):
        if not arr[x][i]:
            continue
        else:
            if i not in visited:
                result += arr[x][i]
                visited.append(i)
                dfs(x+1,result)
                result -= arr[x][i]
                visited.pop()


for tc in range(int(input())):
    visited = []
    arr = [list(map(int, input().split())) for _ in range(11)]
    _max = 0
    dfs(0,0)
    print(_max)
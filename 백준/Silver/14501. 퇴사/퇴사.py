n = int(input())
arr = [0]
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a,b))
_max = 0
def dfs(x,result):
    global _max
    if x == n+1:
        if result > _max:
            _max = result
        return
    if arr[x][0] == 1:
        result += arr[x][1]
        dfs(x+1,result)
    elif x+arr[x][0]-1 <= n:
        result += arr[x][1]
        dfs(x+arr[x][0],result)
        result -= arr[x][1]
    else:
        dfs(x + 1, result)
    dfs(x + 1, result)
dfs(1,0)
print(_max)

import sys
sys.setrecursionlimit(100000)
n, m, k = map(int, input().split())
arr = [[1] * m for _ in range(n)]
result = []
for _ in range(k):
    li = [*map(int, input().split())]
    for i in range(li[0], li[2]):
        for j in range(li[1], li[3]):
            arr[j][i] = 0
cnt = 0
def dfs(x, y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if arr[x][y]:
        cnt += 1
        arr[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1
            result.append(cnt)
            cnt = 0
print(count)
print(*sorted(result))
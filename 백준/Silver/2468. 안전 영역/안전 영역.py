import copy
import sys
sys.setrecursionlimit(100000)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
rain = 0
result = []


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if city[x][y] != 0:
        city[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


while rain < 100:
    count = 0
    city = copy.deepcopy(arr)
    for i in range(n):
        for j in range(n):
            if city[i][j] <= rain:
                city[i][j] = 0
    for i in range(n):
        for j in range(n):
            if dfs(i, j):
                count += 1
    result.append(count)
    rain += 1
print(max(result))

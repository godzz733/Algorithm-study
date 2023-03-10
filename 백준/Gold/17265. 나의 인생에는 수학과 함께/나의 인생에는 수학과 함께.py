import sys

sys.setrecursionlimit(100000)

n = int(input())
arr = [list(map(str, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []
li = []
num_arr = []
def dfs(x, y):
    global li
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if not visited[x][y]:
        li.append(arr[x][y])
        visited[x][y] = True
        dfs(x + 1, y)
        dfs(x, y + 1)
        visited[x][y] = False #만약 도착 했다면 방문기록을 없애줌
        result.append(li[:])
        li.pop() # 경로도 수정
        return True
    return False

dfs(0,0)
for i in result: #여기는 그냥 계산때문에 있는거라 신경 안써도 됨
    a = 0
    if len(i) == (n * 2 - 1):
        a = int(i[0])
        for k in range(1,n*2-1,2):
            if i[k] == '*':
                a *= int(i[k+1])
            elif i[k] == '-':
                a -= int(i[k+1])
            elif i[k] == '+':
                a += int(i[k+1])
        num_arr.append(a)
print(max(num_arr),min(num_arr))

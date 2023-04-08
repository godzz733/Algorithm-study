import math
n = int(input())
arr = [[0] * n for _ in range(n)]
lst = []
for _ in range(n):
    a, b = map(int,input().split())
    lst.append((a,b))
for i in range(n):
    for j in range(n):
        if i!=j:
            arr[i][j] = math.sqrt((lst[i][0]-lst[j][0])**2 + (lst[i][1]-lst[j][1])**2)

arrive = (1<<n) - 1
visited = [[None] * (1<<n) for _ in range(n)]
INF = float('inf')
def find_path(last,visit):
    if visit == arrive:
        return arr[last][0] or INF

    if visited[last][visit] is not None:
        return visited[last][visit]
    temp= INF
    for city in range(n):
        if visit & (1<<city) == 0 and arr[last][city]:
            temp = min(temp, find_path(city, visit | (1<<city)) + arr[last][city])
    visited[last][visit] = temp
    return temp
print(find_path(0,1<<0))
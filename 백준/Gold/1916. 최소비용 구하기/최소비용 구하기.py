import sys
input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())
INF = int(1e9)
arr = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)
for _ in range(m):
    a,b,c = map(int, input().rstrip().split())
    arr[a].append((b,c))
x,y = map(int,input().split())
start = x
end = y
def current_node():
    _min = int(1e9)
    index = 0
    for i in range(1,n+1):
        if not visited[i] and _min>distance[i]:
            _min = distance[i]
            index = i
    return index
def dik(start):
    distance[start] = 0
    visited[start] = True
    for i in arr[start]: #한 도시에서 다른 도시로 갈 떄 버스가 한개인가?
        if distance[i[0]] > i[1]:
            distance[i[0]] = i[1]
    for i in range(n-1):
        now = current_node()
        visited[now] = True
        for j in arr[now]:
            cost = distance[now] + j[1]
            if distance[j[0]] > cost:
                distance[j[0]] = cost
dik(start)
print(distance[end])
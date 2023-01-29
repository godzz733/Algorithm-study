import sys
input = sys.stdin.readline
n = int(input().rstrip())
t = int(input().rstrip())
visited = [False] * (n+1)
distance = [0] * (n+1)
arr = [[] for _ in range(n+1)]
for _ in range(t):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(arr,start,distance,visited):
    visited[start] =True
    for i in arr[start]:
        distance[i] = 1
    for i in arr[start]:
        if not visited[i]:
            dfs(arr,i,distance,visited)
dfs(arr,1,distance,visited)
count = 0
distance[1] = 0
for i in distance:
    if i>0:
        count +=1
print(count)





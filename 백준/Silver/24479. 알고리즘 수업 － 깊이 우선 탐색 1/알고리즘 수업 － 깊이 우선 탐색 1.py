import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n,m,start = map(int,input().split())
arr = [[] for _ in range(n+1)]
node = [i for i in range(1,n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(1,n+1):
    arr[i] = sorted(arr[i])
dic = {}
count = 0
def dfs(arr,visited,start):
    global count
    count +=1
    visited[start] = True
    dic[start] = count

    for i in arr[start]:
        if not visited[i]:
            dfs(arr,visited,i)

dfs(arr,visited,start)
for i in node:
    if i not in dic:
        dic[i] = 0
dic = dict(sorted(dic.items(),key=lambda x:x[0]))
for i in dic.values():
    print(i)
    
import sys;input = sys.stdin.readline
n,m,k = map(int,input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [False]*(n+1)
visited2 = [False]*(n+1)
for _ in range(k):
    tem = int(input())
    ans = 0
    if visited2[tem]:
        print(0)
        continue
    visited2[tem] = True
    if not visited[tem]:
        ans += 1
        visited[tem] = True
    for i in arr[tem]:
        if not visited[i]:
            ans += 1
            visited[i] = True
    print(ans)
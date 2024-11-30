import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
arr = [[0,0] for _ in range(n+1)]
for _ in range(n):
    a,b,c = map(int,input().rstrip().split())
    arr[a][0] = b
    arr[a][1] = c

ans = 0
num = 0
def dfs(now):
    global ans,num
    if arr[now][0] != -1:
        ans += 2
        dfs(arr[now][0])
    num += 1
    solve()
    if arr[now][1] != -1:
        ans += 1
        dfs(arr[now][1])
        ans += 1
def solve():
    if num == n:
        print(ans)
        exit()
dfs(1)
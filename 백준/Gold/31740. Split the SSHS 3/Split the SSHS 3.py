import sys; input = sys.stdin.readline
n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
num = [0] + [int(input()) for _ in range(n)]
v = [0]*(n+1)
p = [0]*(n+1)   
def tree(x,pre):
    v[x] = 1
    p[x] = pre
    for i in arr[x]:
        if v[i]: continue
        num[x] += tree(i,x)
    return num[x]
tree(1,0)
ans = [987654321,0]
for i in range(2,n+1):
    if abs(num[1]-2*num[i]) < ans[0]:
        ans[0] = abs(num[1] - 2*num[i])
        ans[1] = i
print(ans[0])
print(p[ans[1]],ans[1])
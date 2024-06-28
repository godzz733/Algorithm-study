import sys; input = sys.stdin.readline
n,m = map(int,input().split())
arr = []

for _ in range(m):
    a,b,c = map(int,input().split())
    arr.append((c,a,b))
    arr.append((c,b,a))

arr.sort(key=lambda x: x[0])

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
ans = 0
while arr:
    c,a,b = arr.pop()
    if find(a) != find(b):
        union(a,b)
        ans += c
for i in range(2,n+1):
    if find(i) != find(1):
        ans = -1
        break

print(ans)
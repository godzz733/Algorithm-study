def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a<b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

v,e = map(int, input().split())
arr = []
parent = [0] * (v+1)
for i in range(1,v+1):
    parent[i] = i
for _ in range(e):
    a, b, cost = map(int,input().split())
    arr.append((cost,a,b))
arr.sort()
result = 0
for cost,a,b in arr:
    if find_parent(a) != find_parent(b):
        union_parent(a,b)
        result += cost
print(result)

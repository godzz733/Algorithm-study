def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    parent = [0] * (n+1)

    for i in range(0, n+1):
        parent[i] = i
    
    for _ in range(m):
        a, b = map(int, input().split())
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
    del parent[0]
    print(len(parent)-1)
import sys;input = sys.stdin.readline
import heapq as heq
n = int(input())
q = []
lst = []
for i in range(n):
    a,b = map(float,input().split())
    lst.append((a,b))
for i in range(n-1):
    for j in range(i+1,n):
        a,b = lst[i]
        c,d = lst[j]
        heq.heappush(q,(round(((a-c)**2+(b-d)**2)**0.5,2),i,j))
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
def union(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

ans = 0
parent = [i for i in range(n+1)]
while q:
    c,a,b = heq.heappop(q)
    if find_parent(a) != find_parent(b):
        union(a,b)
        ans += c
print(ans)
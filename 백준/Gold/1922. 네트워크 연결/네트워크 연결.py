import sys;input = sys.stdin.readline
import heapq as heq
n = int(input())
q = []
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    heq.heappush(q,(c,a,b))
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
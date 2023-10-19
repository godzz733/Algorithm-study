import sys;input = sys.stdin.readline
import heapq as heq
n = int(input())
q = []
lst = []
for i in range(n):
    a,b,c = map(int,input().split())
    lst.append((a,b,c,i))
lst.sort(key = lambda x:x[0])
for i in range(n-1):
    heq.heappush(q,(abs(lst[i][0]-lst[i+1][0]),lst[i][3],lst[i+1][3]))
lst.sort(key = lambda x:x[1])
for i in range(n-1):
    heq.heappush(q,(abs(lst[i][1]-lst[i+1][1]),lst[i][3],lst[i+1][3]))
lst.sort(key = lambda x:x[2])
for i in range(n-1):
    heq.heappush(q,(abs(lst[i][2]-lst[i+1][2]),lst[i][3],lst[i+1][3]))

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
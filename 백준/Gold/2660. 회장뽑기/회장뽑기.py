import sys
input = sys.stdin.readline
def friends(s):
    visited = [0] * (V + 1)
    q = [(s, 0)]
    visited[s] = 1
    while q:
        v, cnt = q.pop(0)
        for w in graph[v]:
            if not visited[w]:
                visited[w] = 1
                q.append((w, cnt+1))
    candidates.append((s, cnt))

V = int(input())
graph = [[] for _ in range(V)]
while 1:
    a, b = map(int, input().split())
    if a == -1:
        break
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

candidates = []
for i in range(0, V):
    friends(i)
candidates.sort(key=lambda x: (x[1], x[0]))

final_voted = candidates[0][1]
final_cnt = 0
final_candidiates = []
for i in range(V):
    if candidates[i][1] == final_voted:
        final_cnt += 1
        final_candidiates.append(candidates[i][0]+1)

print(final_voted, final_cnt)
print(*final_candidiates)
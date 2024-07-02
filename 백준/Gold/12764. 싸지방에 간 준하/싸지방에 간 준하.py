import sys; input = sys.stdin.readline
import heapq as h
n = int(input())
q = []
c = []
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())) + [i])

arr.sort()
idx = 0
dic = {}
for x,y,z in arr:
    while q:
        t1,t2 = h.heappop(q)
        if t1 > x:
            h.heappush(q,[t1,t2])
            break
        h.heappush(c,t2)
    if not c:
        h.heappush(q,[y,idx])
        dic[idx] = 1
        idx += 1
    else:
        t = h.heappop(c)
        h.heappush(q,[y,t])
        dic[t] += 1
print(len(dic))
print(*[i[1] for i in sorted(dic.items())])
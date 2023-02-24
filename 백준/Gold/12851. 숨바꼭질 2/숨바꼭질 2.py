from collections import deque
result = [0] * (200001)
n, m = map(int, input().split())
result[n] = 1
key = cnt = 0
q = deque()
visited = set()
lst = set()
lst.add(n)
visited.add(n)
while lst:
    q.extend(lst)
    cnt += 1
    for i in lst:
        visited.add(i)
    lst.clear()
    while q:
        x = q.popleft()
        if x == m:
            key += 1
            continue
        else:
            if 0<=x<100001:
                if x-1 not in visited:
                    lst.add(x-1)
                    result[x-1] += result[x]
                if x+1 not in visited:
                    lst.add(x+1)
                    result[x+1] += result[x]
                if x*2 not in visited and x*2<100001:
                    lst.add(x*2)
                    result[x*2] += result[x]
    if key:
        break
print(cnt - 1)
print(result[m])

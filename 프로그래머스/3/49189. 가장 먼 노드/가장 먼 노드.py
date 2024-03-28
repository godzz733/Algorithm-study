import heapq as h
def solution(n, edge):
    answer = 0
    q = []
    arr = [[] for _ in range(n+1)]
    for x,y in edge:
        arr[x].append((y,1))
        arr[y].append((x,1))
    ans = [int(1e9)] * (n+1)
    h.heappush(q,(1,0))
    ans[1] = 0
    while q:
        now,dist = h.heappop(q)
        if ans[now] < dist: continue
        for x,y in arr[now]:
            cost = dist + y
            if ans[x] > cost:
                ans[x] = cost
                h.heappush(q,(x,cost))
    return ans.count(max(ans[1:]))
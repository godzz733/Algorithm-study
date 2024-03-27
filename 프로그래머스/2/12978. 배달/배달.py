import heapq as h
def solution(N, road, K):
    answer = 0
    q = []
    arr = [[] for _ in range(N+1)]
    for a,b,c in road:
        arr[a].append((b,c))
        arr[b].append((a,c))
    ans = [int(1e9)] * (N+1)
    ans[1] = 0
    h.heappush(q,(1,0))
    while q:
        now,dist = h.heappop(q)
        if ans[now] < dist:
            continue
        for x,y in arr[now]:
            cost = y + dist
            if ans[x] >= cost:
                ans[x] = cost
                h.heappush(q,(x,cost))
    for i in ans[1:]:
        if i <= K: answer += 1
    return answer
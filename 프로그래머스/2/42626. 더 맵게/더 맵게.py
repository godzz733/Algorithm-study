import heapq as h
def solution(scoville, K):
    answer = 0
    h.heapify(scoville)
    try:
        while 1:
            x = h.heappop(scoville)
            if x>=K: break
            y = h.heappop(scoville)
            answer += 1
            h.heappush(scoville,x + (y << 1))
    except:
        return -1
    return answer
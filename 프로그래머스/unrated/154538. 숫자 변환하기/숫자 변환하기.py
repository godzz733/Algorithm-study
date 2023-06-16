from collections import deque
def solution(x, y, n):
    _set = set()
    answer = -1
    q = deque()
    if x==y:
        return 0
    q.append((x,0))
    while q:
        x, cnt = q.popleft()
        if x*2 not in _set and x*2 < 1000001:
            if x*2 == y: return cnt+1
            q.append((x*2,cnt+1))
            _set.add(x*2)
        if x*3 not in _set and x*3 < 1000001:
            if x*3 == y: return cnt+1
            q.append((x*3,cnt+1))
            _set.add(x*3)
        if x+n not in _set and x+n < 1000001:
            if x+n == y: return cnt+1
            q.append((x+n,cnt+1))
            _set.add(x+n)
    return answer
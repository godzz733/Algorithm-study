from collections import deque
for _ in range(int(input())):
    a = input()
    n = int(input())
    arr = list(input().replace('[','').replace(',',' ').replace(']','').split())
    q= deque()
    q.extend(arr)
    key = 0
    ans = 0
    for i in a:
        if i == "R":
            key ^= 1
        else:
            if not len(q):
                ans = 'error'
                break
            else:
                if not key:
                    q.popleft()
                else:
                    q.pop()
    if ans:
        print(ans)
    else:
        ans = '['
        if key == 0:
            while len(q)>1:
                ans += q.popleft() + ','
            if q:
                ans += q.popleft()
        else:
            while len(q)>1:
                ans += q.pop() + ','
            if q:
                ans += q.pop()
        ans += ']'
        print(ans)
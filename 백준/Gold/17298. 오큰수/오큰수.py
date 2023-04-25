from collections import deque
n = int(input())
arr = list(map(int,input().split()))
result = [-1] * n
q = deque()
_min = 0
for i in range(n):
    if not q:
        q.append((arr[i],i))
        continue
    else:
        if arr[i] <= _min:
            _min = arr[i]
            q.append((arr[i],i))
        else:
            while q:
                num, idx = q.pop()
                if num>=arr[i]:
                    q.append((num,idx))
                    break
                else:
                    result[idx] = arr[i]
            q.append((arr[i], i))
print(*result)
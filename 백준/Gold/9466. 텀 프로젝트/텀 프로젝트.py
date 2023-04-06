from collections import deque
def bfs(i):
    if dp[i]:
        return
    global ans
    q = deque()
    q.append(i)
    visited = set()
    visited.add(i)
    dele = []
    dele.append(i)
    while q:
        x = q.popleft()
        if arr[x] == i:
            for x in visited:
                dp[x] = x
            break
        if dp[arr[x]]:
            ans += 1
            dp[i] = 100
            return
        elif arr[x] in visited:
            dp[i] = 100
            while 1:
                a = dele.pop()
                dp[a] = 100
                if a == arr[x]:
                    break
            ans += len(dele)
            for i in dele:
                dp[i] = 100
            return
        else:
            q.append(arr[x])
            visited.add(arr[x])
            dele.append(arr[x])
for tc in range(int(input())):
    n = int(input())
    arr = [0] + list(map(int,input().split()))
    ans = 0
    dp = [0] * (n+1)

    for i in range(1,n+1):
        if i == arr[i]:
            dp[i] = i
            continue

        if not dp[i]:
            bfs(i)

    print(ans)


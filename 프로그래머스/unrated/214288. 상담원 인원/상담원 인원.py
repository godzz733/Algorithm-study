import heapq as q
arr = []
dp = []
ans = 987654321
def solution(k, n, reqs):
    global arr,dp,ans
    answer = 0
    arr = [[] for _ in range(k)]
    for a,b,c in reqs:
        arr[c-1].append((a,b))
    dp = [[0] * (n-k+1) for _ in range(k)]
    for i in range(k):
        for j in range(1,n-k+2):
            dp[i][j-1] = func(arr[i],j)
    back(0,0,0,n-k+2,n,k)
    print(dp)
    answer = ans
    return answer

def func(arr,n):
    last = []
    ans = 0
    for i in range(len(arr)):
        if len(last) < n:
            q.heappush(last,(sum(arr[i]),i))
        else:
            x = q.heappop(last)
            if x[0] > arr[i][0]:
                ans += x[0]-arr[i][0]
                q.heappush(last,(x[0] + arr[i][1],i))
            else:
                q.heappush(last,(sum(arr[i]),i))
    return ans if ans > 0 else 0

def back(idx,many,cnt,num,n,k):
    global dp,ans
    if idx == k:
        if many <= n:
            ans = min(ans,cnt)
        return
    for i in range(1,num):
        back(idx+1,many + i,cnt + dp[idx][i-1],num,n,k)
        
    
    
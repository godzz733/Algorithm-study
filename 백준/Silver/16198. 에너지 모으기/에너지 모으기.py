import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
ans = 0
def back(arr,cnt):
    global ans
    if len(arr)<3:
        ans = max(ans,cnt)
        return
    for i in range(1,len(arr)-1):
        back(arr[:i]+arr[i+1:],cnt+arr[i-1]*arr[i+1])
back(arr,0)
print(ans)
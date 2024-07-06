import sys; input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
ans = sum(arr[n//2+1:])
for i in range(n//2+1):
    ans += arr[i]//2
print(ans)
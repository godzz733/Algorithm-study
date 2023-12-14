import sys;input = sys.stdin.readline
n,m = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
arr = [0]*(3000)
for i in a:
    arr[i] += 1

for i in range(min(a),max(a)+1):
    if arr[i]:
        for j in range(i,i+m):
            arr[j] = 0
        ans += 1
print(ans)
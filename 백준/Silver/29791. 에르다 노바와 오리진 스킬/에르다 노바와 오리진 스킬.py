a,b = map(int,input().split())
ans = [1,1]
arr = list(map(int,input().split()))
arr.sort()
idx = arr[0]
for i in range(1,a):
    if arr[i] - idx < 100: continue
    else:
        ans[0] += 1
        idx = arr[i]
arr = list(map(int,input().split()))
arr.sort()
idx = arr[0]
for i in range(1,b):
    if arr[i] - idx < 360: continue
    else:
        ans[1] += 1
        idx = arr[i]
print(*ans)
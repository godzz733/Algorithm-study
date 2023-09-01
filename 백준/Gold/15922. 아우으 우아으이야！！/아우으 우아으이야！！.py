n = int(input())
arr = [tuple(map(int,input().split())) for _ in range(n)]
arr.sort()
st,fi = arr[0][0],arr[0][1]
ans = 0
for i in range(1,n):
    if arr[i][0] >= st and arr[i][1] <= fi: continue
    elif arr[i][0] >= st and arr[i][0] <= fi and arr[i][1] >= fi: fi = arr[i][1]
    elif arr[i][0] >= st:
        ans += fi-st
        st,fi = arr[i][0],arr[i][1]
ans += fi - st
print(ans)
n = int(input())
arr = []
for i in range(n):
    arr.append(tuple(map(int,input().split())))
arr.sort(key=lambda x: (x[1],x[0]))
ans = 0
now = -1
for i in range(n):
    if now<= arr[i][0]:
        ans += 1
        now = arr[i][1]
print(ans)
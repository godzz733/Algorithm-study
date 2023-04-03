n = int(input())
arr = []
for _ in range(n):
    x, y = map(int,input().split())
    arr.append((x,y))
result = 0
for i in range(n-1):
    result += (arr[i][0]+arr[i+1][0])*(arr[i][1]-arr[i+1][1])
result += (arr[n-1][0]+arr[0][0])*(arr[n-1][1]-arr[0][1])
print("{:.1f}".format(round(abs(result)/2,2)))
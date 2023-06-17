n, m = map(int, input().split())
lst = []
for i in range(m):
    a, b = map(int,input().split())
    lst.append((a,b))
arr = [0] * (n+1)
for x,y in lst:
    for i in range(n,y-1,-1):
        arr[i] = max(arr[i],arr[i-y]+x)
print(arr[-1])
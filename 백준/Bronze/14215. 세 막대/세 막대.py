arr = [*map(int,input().split())]
arr.sort()
if arr[2] >= arr[0]+arr[1]:
    print((arr[0]+arr[1])*2-1)
else:print(sum(arr))

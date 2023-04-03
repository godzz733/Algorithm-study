n = int(input())
arr = [*map(int,input().split())]
result = 2000000000
a = b = 0
arr.sort()
for i in range(n-1):
    st = i+1
    end = n-1
    res = 0
    while st<=end:
        mid = (st+end)//2
        if arr[mid]+arr[i]>0:
            end = mid-1
            if result > abs(arr[mid] + arr[i]):
                result = abs(arr[mid] + arr[i])
                a = arr[i]
                b = arr[mid]
        else:
            st = mid+1
            res = mid
            if result > abs(arr[mid] + arr[i]):
                result = abs(arr[mid] + arr[i])
                a = arr[i]
                b = arr[mid]

print(a,b)


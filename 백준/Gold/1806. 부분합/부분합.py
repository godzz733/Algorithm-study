n,m = map(int,input().split())
arr= [*map(int,input().split())]
result = 1000000
_sum = arr[0]
arr.append(0)
st = 0
end = 1
if max(arr) >= m:
    print(1)
else:
    while st<=end and end<n+1:
        if _sum>=m:
            result = min(result,end-st)
            _sum -= arr[st]
            st += 1
        else:
            _sum += arr[end]
            end += 1
    if result == 1000000:
        print(0)
    else:
        print(result)


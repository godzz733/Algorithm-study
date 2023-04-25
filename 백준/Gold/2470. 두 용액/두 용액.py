n = int(input())
arr = [*map(int,input().split())]
arr.sort()

result = 2000000001
result_idx = [0,0]
def binary(start,end,num):
    global result, result_idx
    ans = 0
    while start<=end:
        mid = (start+end)//2
        if num+arr[mid] > 0:
            end = mid-1
            if result > abs(num + arr[mid]):
                result = abs(num + arr[mid])
                result_idx = [num, arr[mid]]
        else:
            start = mid + 1
            if result > abs(num + arr[mid]):
                result = abs(num + arr[mid])
                result_idx = [num, arr[mid]]



for i in range(n-1):
    binary(i+1,n-1,arr[i])
print(*result_idx)
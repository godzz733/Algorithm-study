import sys
input = sys.stdin.readline
a,b = map(int, input().split())
arr = [*map(int,input().split())]
start = 0
end = max(arr)
result = 0
try:
    while start<=end:
        num = 0
        mid = (start+end)//2
        for i in arr:
            num += i//mid
        if num<a:
            end = mid-1
        else:
            start = mid +1
            result = mid
    print(result)
except:
    print(0)
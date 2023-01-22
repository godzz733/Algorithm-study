import sys
k, n =map(int, sys.stdin.readline().split())
arr = []
result = 0
final =0
for _ in range(k):
    a = int(sys.stdin.readline())
    arr.append(a)
low = 1
high= max(arr)
if n ==1:
    result = max(arr)-1
else:
    while 1:
        num = 0
        test = 0
        mid = (low+high)//2
        for k in arr:
            num+=k//mid
        if num<n:
            if high == low+1:
                result = low
                break
            else:
                high = mid
        elif num>=n:
            if high == low+1:
                result = low
                break
            else:
                low = mid
        if result!=0:
            break
num = 0
for i in arr:
    num += i//(result+1)
if num == n:
    result+=1
       
print(result)


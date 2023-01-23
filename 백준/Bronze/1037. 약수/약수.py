t = int(input())
arr = [*map(int, input().split())]
a = max(arr)
b = min(arr)
if t==1:
    print(arr[0]*arr[0])
else:
    print(a*b)
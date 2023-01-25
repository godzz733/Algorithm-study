import sys
t = int(input())
arr = [*map(int,sys.stdin.readline().split())]
test = arr[::]
# arr_minus
for i in range(1,t):
    if arr[i-1] + arr[i] >0:
        arr[i] = arr[i-1] + arr[i]
    else:
        arr[i] = 0
if sum(arr)==arr[0]:
    print(max(test))
else:
    print(max(arr))

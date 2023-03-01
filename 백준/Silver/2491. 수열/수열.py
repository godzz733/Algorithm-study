n = int(input())
arr = [*map(int,input().split())]
_max = 0
increase = 1
decrease = 1
for i in range(n-1):
    if arr[i+1] >= arr[i]:
        increase += 1
    else:
        if _max < increase:
            _max = increase
            increase = 1
        else:
            increase = 1
if _max < increase:
    _max = increase
for i in range(n-1):
    if arr[i+1] <= arr[i]:
        decrease += 1
    else:
        if _max < decrease:
            _max = decrease
            decrease = 1
        else:
            decrease = 1
if _max < decrease:
    _max = decrease
print(_max)



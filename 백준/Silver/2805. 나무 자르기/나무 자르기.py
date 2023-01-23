import sys
n,m = map(int , input().split())
arr = [*map(int,sys.stdin.readline().split())]
tree = []
result = 0
low = 0
high = max(arr)
while 1:
    mid = (low + high)//2
    tree_length = 0
    test = 0
    for i in arr:
        if (i-mid)>0:
            tree_length +=(i-mid)
    if tree_length>=m:
        for i in arr:
            if (i-mid-1)>0:
                test+=(i-mid-1)
        if test<m:
            result = mid
            break
        else:
            low = mid
    else:
        for i in arr:
            if (i-mid+1)>0:
                test+=(i-mid+1)
        if test==m:
            result = (mid -1)
            break
        else:
            high = mid
print(result)
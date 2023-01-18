import sys
n = int(input())
arr1 = [*map(int,sys.stdin.readline().split())]
arr2 = [*map(int,sys.stdin.readline().split())]
num = 0
del arr2[len(arr2)-1]

while 1:
    if arr2.index(min(arr2)) == 0:
        num+= arr2[0] * sum(arr1)
        break
    else:
        arr_min = arr2[arr2.index(min(arr2)):]
        num += sum(arr1[arr2.index(min(arr2)):]) * min(arr2)
        arr1 = arr1[:arr2.index(min(arr2))]
        arr2 = arr2[:arr2.index(min(arr2))]

print(num)
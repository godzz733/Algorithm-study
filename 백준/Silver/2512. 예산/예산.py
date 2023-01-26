import sys
input = sys.stdin.readline
a = int(input())
arr= [*map(int, input().split())]
b = int(input())

min_num = 0 
max_num = max(arr)
result =0
while min_num<=max_num:
    num = 0
    mid = (min_num+max_num)//2

    for i in arr:
        if i>mid:
            num+=mid
        else:
            num+=i
    
    if num>b:
        max_num= mid-1
    else:
        min_num= mid +1
        result = mid
print(result)

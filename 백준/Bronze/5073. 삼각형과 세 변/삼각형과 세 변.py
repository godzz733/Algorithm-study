while 1:
    arr = [*map(int,input().split())]
    if not arr[0]:break
    arr.sort()
    if arr[2] >= arr[0]+arr[1]:print("Invalid")
    elif arr[0] == arr[1] == arr[2]:print("Equilateral")
    elif arr[0] == arr[1] or arr[1] == arr[2]:print("Isosceles")
    else:print("Scalene")
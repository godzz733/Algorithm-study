t = int(input())
for i in range(t):
    a = int(input())
    arr = [0]* (100+1)
    arr[1] = 1
    arr[2] = 1
    arr[3] = 1
    if a==1 or a==2 or a==3:
        print(1)
    else:
        for k in range(4,a+1):
            arr[k] = arr[k-3] + arr[k-2]
        print(arr[a])
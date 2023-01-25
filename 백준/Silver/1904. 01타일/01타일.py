t = int(input())
arr = [0] * (t+2)
arr[1] = 1
arr[2] = 2
if t==1:
    print(1)
elif t==2:
    print(2)
else:
    for i in range(3,t+1):
        arr[i] = (arr[i-1] + arr[i-2])%15746
    print(arr[t])
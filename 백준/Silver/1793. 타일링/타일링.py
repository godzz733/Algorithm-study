arr = [1,1]
for i in range(2,251): arr.append(arr[i-1] + arr[i-2]*2)
while 1:
    try:print(arr[int(input())])
    except:break
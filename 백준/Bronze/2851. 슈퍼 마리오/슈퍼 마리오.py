import sys
input = sys.stdin.readline
arr= []
for _ in range(10):
    arr.append(int(input().rstrip()))
num = 0
result = []
if arr[0]>=100:
    print(arr[0])
else:
    for i in range(10):
        num += arr[i]
        if num>=100:
            result.append(num)
            result.append(num-arr[i])
            break
    if num<100:
        print(num)
    else:
        if abs(result[0]-100) > abs(result[1]-100):
            print(result[1])
        elif abs(result[0]-100) < abs(result[1]-100):
            print(result[0])
        else:
            print(result[0])

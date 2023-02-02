import sys

inp = sys.stdin.readline
t = int(inp())
arr = []
for _ in range(6):
    n, m = map(int, inp().rstrip().split())
    arr.append((n, m))
arr1 = [4, 2, 3, 1, 3, 1]
arr2 = [2, 3, 1, 4, 1, 4]
arr3 = [3, 1, 4, 2, 4, 2]
arr4 = [1, 4, 3, 2, 3, 2]
num1 = 0
num2 = 0
num3 = 0
num4 = 0
result = []
num = 0
idx = 0
for i in arr:
    if i[0] == 1:
        num1 += 1
    elif i[0] == 2:
        num2 += 1
    elif i[0] == 3:
        num3 += 1
    elif i[0] == 4:
        num4 += 1
if num2 == num4 == 1:
    for i in range(6):
        if arr[i][0] == 4:
            idx = i
    while len(result) < 6:
        result.append(arr[idx][1])
        idx += 1
        if idx >= 6:
            idx = 0


elif num2 == num3 == 1:
    for i in range(6):
        if arr[i][0] == 2:
            idx = i
    while len(result) < 6:
        result.append(arr[idx][1])
        idx += 1
        if idx >= 6:
            idx = 0
elif num1 == num3 == 1:
    for i in range(6):
        if arr[i][0] == 3:
            idx = i
    while len(result) < 6:
        result.append(arr[idx][1])
        idx += 1
        if idx >= 6:
            idx = 0
elif num1 == num4 == 1:
    for i in range(6):
        if arr[i][0] == 1:
            idx = i
    while len(result) < 6:
        result.append(arr[idx][1])
        idx += 1
        if idx >= 6:
            idx = 0

print(((result[0]*result[1])-(result[3]*result[4]))*t)
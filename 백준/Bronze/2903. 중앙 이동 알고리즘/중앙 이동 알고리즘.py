arr = [2]
for i in range(15):arr.append(arr[-1] * 2 -1)
print(arr[int(input())]**2)
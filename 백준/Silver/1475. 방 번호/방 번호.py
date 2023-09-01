arr = [0] * 10
for i in input():
    if int(i) == 6 or int(i) == 9: arr[6] += 0.5
    else:arr[int(i)] += 1
print(int(max(arr)+0.5))
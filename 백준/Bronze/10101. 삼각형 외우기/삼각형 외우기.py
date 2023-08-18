arr = []
for _ in range(3):
    arr.append(int(input()))
arr.sort()
if arr.count(60) == 3: print("Equilateral")
elif sum(arr) != 180: print("Error")
else:
    if arr[0] == arr[1] or arr[1] == arr[2]: print("Isosceles")
    else: print("Scalene")
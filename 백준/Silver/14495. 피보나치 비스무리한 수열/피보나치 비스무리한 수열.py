n = int(input())
arr = [0,1,1,1]
for i in range(4, n+1):arr.append(arr[i-1]+arr[i-3])
print(arr[n])
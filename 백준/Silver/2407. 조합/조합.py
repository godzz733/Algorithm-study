import sys
input = sys.stdin.readline
a,b = map(int,input().split())
arr = [0 for _ in range(101)]
arr[1] = 1
for i in range(2,101):
    arr[i] = arr[i-1] * i
num = arr[a]//(arr[b]*arr[a-b])
print(int(num))


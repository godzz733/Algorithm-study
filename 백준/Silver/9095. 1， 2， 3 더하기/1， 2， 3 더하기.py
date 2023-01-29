import sys
input = sys.stdin.readline
n = int(input().rstrip())
for _ in range(n):
    t = int(input().rstrip())
    arr = [0] * 12
    arr[1] = 1
    arr[2] = 2
    arr[3] = 4
    for i in range(4,t+1):
        arr[i] = arr[i-3] + arr[i-2] + arr[i-1]
    print(arr[t])



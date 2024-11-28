import sys; input = sys.stdin.readline
arr = [i for i in range(10001)]
for i in range(2,101):
    t = i**2
    for j in range(10001-t):
        arr[t+j] = min(arr[t+j],arr[j]+1)

for i in range(int(input())):
    n = int(input())
    print(f"Case #{i+1}: {arr[n]}")
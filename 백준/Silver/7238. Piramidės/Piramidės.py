import sys;input = sys.stdin.readline
n = int(input())
arr = [0]
for i in range(1,1415):
    arr.append(arr[-1] + i)
st = 1414
while n:
    if arr[st] <= n:
        print(st)
        n -= arr[st]
    else:
        st -= 1

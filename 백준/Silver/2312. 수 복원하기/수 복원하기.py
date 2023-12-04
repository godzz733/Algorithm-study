import sys;input = sys.stdin.readline
n = int(input())
for _ in range(n):
    k = int(input())
    ori = k
    arr = [0] * 100001
    idx = 2
    while k != 1:
        if k % idx == 0:
            k //= idx
            arr[idx] += 1
        else:
            idx += 1
    for i in range(2, ori+1):
        if arr[i] != 0:
            print(i, arr[i])
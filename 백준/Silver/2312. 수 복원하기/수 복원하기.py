import sys;input = sys.stdin.readline
n = int(input())
prime = [True] * 100001
prime[0] = prime[1] = False
for i in range(2, 100001):
    if prime[i]:
        for j in range(i+i, 100001, i):
            prime[j] = False
for _ in range(n):
    k = int(input())
    if prime[k]:
        print(k, 1)
        continue
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
import sys;input = sys.stdin.readline
n = int(input())
# ans = 0
# for i in range(1,n+1):
#     tem = 2
#     while not i%2:
#         i //= 2
#         tem *= 2
#     ans += tem
arr = [0,16]
for i in range(3,32):
    arr.append(arr[-1]*2 + (1<<i))
lst = []
a = 0
while n:
    tem = 0
    t = 4
    while n:
        if n < 4:
            if n == 1: a += 2
            elif n == 2: a += 6
            elif n == 3: a += 8
            n = 0
            break
        while n >= t:
            t <<= 1
            tem += 1
        lst.append(tem)
        n -= t>>1
        tem = 0
        t = 4
for i in lst:
    a += arr[i]
print(a)
import sys; input = sys.stdin.readline
n = int(input())
_sum = 1
for i in range(2, 10**6):
    _sum += i
    if _sum > n:
        break
    if (n-_sum) % i == 0:
        t = (n-_sum) // i
        print(t+1, t+i)
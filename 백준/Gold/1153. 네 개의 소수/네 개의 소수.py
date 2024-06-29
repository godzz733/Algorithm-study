import sys; input = sys.stdin.readline

n = int(input())
if n < 8:
    print(-1)
    exit()

prime = [False, False] + [True] * (n-1)
primes = []

for i in range(2, n+1):
    if prime[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            prime[j] = False

ans = []

if n & 1:
    ans.extend([2, 3])
    n -= 5
else:
    ans.extend([2, 2])
    n -= 4

for i in range(len(primes)):
    if prime[n-primes[i]]:
        ans.extend([primes[i], n-primes[i]])
        print(*ans)
        exit() 
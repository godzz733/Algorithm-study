import sys; input = sys.stdin.readline
from itertools import permutations
n = int(input())
prime = [True] * (10000000)
primes = set()
for i in range(2,10000000):
    if prime[i]:
        primes.add(i)
        for j in range(i*i,10000000,i):
            prime[j] = False

for _ in range(n):
    n = list(input().rstrip())
    ans = set()
    for i in range(1,len(n)+1):
        for j in permutations(n,i):
            tmp = int(''.join(j))
            if tmp in primes:
                ans.add(tmp)
    print(len(ans))
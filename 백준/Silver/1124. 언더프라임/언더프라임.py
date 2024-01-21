import sys; I = sys.stdin.readline
prime = [False, False] + [True] * 100000
primes = []
for i in range(2,50001):
    if prime[i]:
        primes.append(i)
        for j in range(i*i,100001,i):
            prime[j] = False
_set = set(primes)
n,m = map(int,I().split())
ans = 0
for i in range(n,m+1):
    tem = 0
    if i in _set:
        continue
    for j in primes:
        while i%j == 0:
            tem += 1
            i //= j
            if i == 1:
                break
        if i == 1:
            break
    if tem in _set:
        ans += 1
print(ans)
import sys; input = sys.stdin.readline

p = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

n = int(input())
if n == 8:
    print("2 2 2 2")
    exit()
if n < 9:
    print(-1)
    exit()
prime = [False, False] + [True] * (n-1)
primes = []
ans = []
for i in range(2, n+1):
    if prime[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            prime[j] = False
idx = len(primes)-1
while n-primes[idx] < 7:
    idx -= 1
ans.append(primes[idx])
n -= primes[idx]

for i in range(25):
    if p[i] > n:
        break
    for j in range(25):
        if p[i] + p[j] > n:
            break
        for k in range(25):
            if p[i] + p[j] + p[k] > n:
                break
            if p[i] + p[j] + p[k] == n:
                ans.append(p[i])
                ans.append(p[j])
                ans.append(p[k])
                print(*sorted(ans))
                exit()
print(-1)
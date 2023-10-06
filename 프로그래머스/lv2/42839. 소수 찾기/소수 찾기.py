from itertools import permutations
def solution(numbers):
    answer = 0
    prime = [True,True] + [False] * (10000000)
    primes = set()
    for i in range(2,10000001):
        if prime[i]:continue
        primes.add(i)
        for j in range(i*2,10000001,i):prime[j] = True
            
    arr = set()
    for i in range(1,len(numbers)+1):
        for j in permutations(numbers,i):
            arr.add(int(''.join(j)))
    for i in arr:
        if i in primes: answer += 1
    return answer
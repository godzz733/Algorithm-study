a,b  =map(int, input().split())
arr = [False,False] + [True]*(b-1) #True, False 사용도 항상 염두할 것
primes = []
for i in range(2,b+1):
    if arr[i]:
        if i>=a:
            primes.append(i)
        for k in range(2*i,b+1,i):
            arr[k] = False

[print(j) for j in primes]



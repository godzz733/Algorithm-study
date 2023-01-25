while 1:
    t = int(input())
    if t==0:
        break
    count = 0
    arr = [False,False] + [True]*(2*t+1) 
    primes = []
    for i in range(2,2*t+1):
        if arr[i]:
            primes.append(i)
            for k in range(2*i,2*t+1,i):
                arr[k] = False

    for i in primes:
        if t<i<=2*t:
            count +=1
    print(count)
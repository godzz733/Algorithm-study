a = int(input())
for k in range(a):
    t = int(input())
    arr = [False,False] + [True]*(10000) 
    primes = []
    result = []
    left = []
    right = []
    middle = []
    min = int(1e9)
    for k in range(2,10000):
        if arr[k]:
            primes.append(k)
            for k in range(2*k,10000,k):
                arr[k] = False
    for i in primes:
        if i <(t/2):
            left.append(i)
        elif i==int(t/2):
            middle.append(i)
        else:
            right.append(i)
    if middle!=[]:
        print(middle[0],middle[0])
    else:
        for i in range(int(t/2)):
            if (int(t/2)-i) in left and (int(t/2)+i) in right:
                print((int(t/2)-i),(int(t/2)+i))
                break


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
                arr[k] = False             #에라토스테네스의 체
    for i in primes: 
        if i <(t/2): #만약 t/2보다 작은 소수라면 left리스트에 추가
            left.append(i)
        elif i==int(t/2): #만약 t/2과 같은 소수라면 middle리스트에 추가
            middle.append(i)
        else: #만약 t/2보다 큰 소수라면 right리스트에 추가
            right.append(i)
    if middle!=[]: #만약 middle이 있다면 그 합이 차이가 가장 작은거
        print(middle[0],middle[0])
    else: # t/2에서 한칸씩 갈때 그 조합이 소수의 합 조합이라면 그게 정답이다.
        for i in range(int(t/2)):
            if (int(t/2)-i) in left and (int(t/2)+i) in right:
                print((int(t/2)-i),(int(t/2)+i))
                break


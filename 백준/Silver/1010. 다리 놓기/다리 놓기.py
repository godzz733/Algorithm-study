for _ in range(int(input())):
    a,b = map(int,input().split())
    ans = 1
    for i in range(b-a+1,b+1):
        ans *= i
    for i in range(1,a+1):
        ans //= i
    print(ans)

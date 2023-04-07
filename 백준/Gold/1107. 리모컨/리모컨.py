n = int(input())
t = int(input())
if not t:
    print(min(abs(n-100),len(str(n))))
else:
    if n == 100:
        print(0)
    else:
        arr = list(map(int, input().split()))
        lst = [i for i in range(1000000)]
        result = abs(n-100)
        for i in lst:
            for k in str(i):
                if int(k) in arr:
                    break
            else:
                if result > abs(n-i) + len(str(i)):
                    result = abs(n-i) + len(str(i))
        print(result)
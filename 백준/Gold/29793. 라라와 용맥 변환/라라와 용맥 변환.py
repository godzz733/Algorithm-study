import sys;input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(input())
ans = 987654321
if m == 1: print(0)
elif m == 2:
    ans = 0
    for i in range(1,n):
        if arr[i] == arr[i-1]:
            ans +=1
            arr[i] = 0
    print(ans)
elif m == 3:
    lst = [list("SRW") * (n//3+1),list("RWS")  * (n//3+1),list("WSR") * (n//3+1),
     list("WRS") * (n//3+1),list("RSW") * (n//3+1),list("SWR") * (n//3+1)]
    for j in lst:
        tem = 0
        for i in range(n):
            if arr[i] != j[i] : tem +=1
        ans = min(ans,tem)
    print(ans)
else:
    if n < 4:
        lst = [list("SRW") * (n//3+1),list("RWS")  * (n//3+1),list("WSR") * (n//3+1),
     list("WRS") * (n//3+1),list("RSW") * (n//3+1),list("SWR") * (n//3+1)]
        for i in lst:
            tem = 0
            for j in range(n):
                if arr[j] != i[j] : tem +=1
            ans = min(ans,tem)
        print(ans)
    else: print(-1)
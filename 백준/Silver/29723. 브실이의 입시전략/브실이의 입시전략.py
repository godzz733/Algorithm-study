n,m,k = map(int,input().split())
dic = {}
arr = []
tem = [tuple(map(str,input().split())) for _ in range(n)]
q = set([input() for _ in range(k)])
ans = 0
for x,y in tem:
    if x in q:
        ans += int(y)
    else:arr.append(int(y))
arr.sort()
print(sum(arr[:m-k])+ans,sum(arr[len(arr)-(m-k):])+ans)